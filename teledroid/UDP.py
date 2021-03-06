#!/usr/bin/env python
'''
Created on Aug 8, 2012

@author: Federico Camoposeco
'''

import threading
import socket
import zlib
import data_pb2
import matches_pb2
import unionProto_pb2
import cv2
import numpy as np
import Queue
import Tkinter as tk

'''
    Class to handle the incoming protobuff messages from the logging
    app. The main loop runs on a sepparate thread in order to be 
    reliably integrated to a Tkinter application. The class will 
    continually write to console. TODO: place output in Tkinter log.
'''

class UDPread(threading.Thread):
    '''
        usage: UDPread(PORT, HOST)
    '''
    def __init__(self, PORT, HOST):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((HOST, PORT))
        self.socket.settimeout(0.25)
        self.endthis = False
        self.finished = False
        self.data = Queue.Queue()
        
    def getData(self, length):
        # non blocking 
        try:
            data, _ = self.socket.recvfrom(length)
            return data
        except socket.timeout:
            pass

    def go(self, root):
        self.root = root
        self.console = tk.StringVar()
        self.showData = tk.StringVar()
        self.showMat  = tk.StringVar()
        self.start()

    def drawKpts(self, kpts, image):
        for kp in kpts:
            cv2.circle(image, (int(kp.ptX), int(kp.ptY)), 2*int(kp.octave+1), (0, 0, 255))
        return image

    def run(self):
        self.accum = '{:<58}'.format('UDP flow monitor online...')
        self.console.set(self.accum)
        i = 0
        chunkNo = 0
        read = False
        first = True;
        sep = '  ________________________________________________________'
        j = 0
        while not self.endthis:
            data = self.getData(15000)
            if data:
                if first:
                    self.accum = '\n'.join((self.accum, sep))
                    self.console.set(self.accum)
                    first = False
                if data[0:4] == 'EXIT':
                    break
                if data[0:16] == 'ProtobuffMessage':
                    chunkNo = int(data.split('_')[1])
                    chunk_i = 0
                    message = ''
                    read = True
                else:
                    if read:
                        message += data
                        chunk_i = chunk_i + 1
                        if chunk_i == chunkNo:
                            chksumA = self.getData(1024)
                            try:
                                intChckA = int(chksumA)
                            except:
                                intChckA = -1
                                read = False
                                fmt = '  {:-^'+str(len(sep)-2)+'}'
                                self.accum = '\n'.join((self.accum, fmt.format('Corrupted data!')))
                                self.console.set(self.accum)
                            chksumB = zlib.crc32(message)& 0xffffffff
                            latestFr = 0;
                            if intChckA == chksumB:
                                i = i + 1
                                frame = data_pb2.FrameProto()
                                matches = matches_pb2.MatchesProto()
                                frame.ParseFromString(message)
                                matches.ParseFromString(message)
                                if frame.seq:
                                    file_name = 'logs/%04d.frs'%i
                                    self.accum = '\n'.join((self.accum,'  frame{:#04} >> {}  |  devId: {:#02}  |  Checksum OK'.format(frame.seq, file_name, frame.id)))
                                    self.console.set(self.accum)
                                    if frame.images:
                                        imageNp = np.fromstring(frame.images[0].bytedata, dtype='uint8')
                                        imgCV = cv2.imdecode(imageNp, 1) # opencv used only for this reason JPEG -> raw
                                        if frame.keypoints:
                                            image = self.drawKpts(frame.keypoints.keypoints, imgCV)
                                        else:
                                            image = imgCV
                                        self.data.put( image ) # put image into a queue
                                    # put metadata into string
                                    meta = frame.metadata
                                    enumDescr = data_pb2.MetadataProto.DESCRIPTOR.enum_types_by_name['SensorType']
                                    l1 = 'VICON (x, y, z) (r, p, y): \n({: 2.3f}, {: 2.3f}, {: 2.3f})\n({: 2.3f}, {: 2.3f}, {: 2.3f})\n'.format(meta.pos_x,meta.pos_y, meta.pos_z, meta.ang_x, meta.ang_y, meta.ang_z)
                                    l2 = '{} SENSOR (x, y, z):\n({: 2.3f}, {: 2.3f}, {: 2.3f})\ntimestamp: {}'.format( enumDescr.values_by_number[meta.type].name, meta.val_0, meta.val_1, meta.val_2, meta.timestamp )
                                    self.showData.set( '\n'.join( (l1,l2) ) )
                                    
                                    # put matrix data into string
                                    matK = frame.cameraMatrix
                                    mat = '{: > 6.1f} {: > 6.1f} {: > 6.1f}\n      {: > 6.1f} {: > 6.1f} {: > 6.1f}\n      {: > 6.1f} {: > 6.1f} {: > 6.1f}'.format(*matK.data)
                                    matC = frame.cameraBodyTrans
                                    mat2 ='{: > 6.3f} {: > 6.3f} {: > 6.3f}\n      {: > 6.3f} {: > 6.3f} {: > 6.3f}\n      {: > 6.3f} {: > 6.3f} {: > 6.3f}'.format(*matC.data)
                                    self.showMat.set('  K:  {: >24}\n\n  R:  {: >24}'.format(mat,mat2))
                                    distCoeffs = frame.distCoeffs
                                    print 'hola'
                                    print distCoeffs.k1, distCoeffs.k2, distCoeffs.k3, distCoeffs.k4, distCoeffs.k5, distCoeffs.k6
                                    # save data
                                    f = open(file_name, 'w')
                                    f.write(message)
                                    f.close
                                    latestFr = frame.seq
                                if matches.imageLseq:
                                    j = j + 1
                                    file_name = 'logs/%03dto%03d.mtc'%(matches.imageLseq, matches.imageRseq)
                                    # self.accum = '\n'.join((self.accum,'   matches  >> {}  |  devId: {:#02}  |  Checksum OK'.format(file_name, matches.id)))
                                    self.accum = '\n'.join((self.accum,'  matches >> {}|  devId: {:#02}  |  Checksum OK'.format(file_name, 3)))
                                    self.console.set(self.accum)
                                    # save data
                                    f = open(file_name, 'w')
                                    f.write(message)
                                    f.close
                                    print "matches"
                            else:
                                self.accum = '\n'.join((self.accum,'  frame{:#04} >> {}  |  devId: {:#02}  |  Checksum!OK'.format(latestFr+1, 'filenotstored', 0)))
                                self.console.set(self.accum)
                            read = False
        self.socket.close()
        self.finished = True
#        fmt = '  {:-^'+str(len(sep)-2)+'}\n'
#        self.accum = '\n'.join((self.accum, fmt.format('Connection terminated.')))
#        self.console.set(self.accum)
        
        
        
        