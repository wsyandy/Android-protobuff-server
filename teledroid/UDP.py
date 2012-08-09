#!/usr/bin/env python
'''
Created on Aug 8, 2012

@author: Federico Camoposeco
'''

import threading
import socket
import zlib
import data_pb2
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
        self.socket.settimeout(1)
        self.consoline = Queue.Queue()
        self.endthis = False
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
        self.start()
          
    def run(self):
        self.accum = 'UDP flow monitor online...'
        self.console.set(self.accum)
        i = 0
        chunkNo = 0
        read = False
        first = True;
        sep = '  ________________________________________________________'
        
        while not self.endthis:
            data = self.getData(15000)
            if data:
                if first:
                    self.consoline.put(sep)
                    first = False
                if data[0:4] == 'EXIT':
                    break
                if data[0:16] == 'ProtobuffMessage':
                    chunkNo = int(data.split('_')[1])
                    chunk_i = 0
                    message = ''
                    read = True
                    i = i + 1
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
                                frame = data_pb2.FrameProto()
                                frame.ParseFromString(message)
                                file_name = 'logs/%04d.frs'%i
                                self.accum = '\n'.join((self.accum,'  frame{:#04} >> {}  |  devId: {:#02}  |  Checksum OK'.format(frame.seq, file_name, frame.id)))
                                self.console.set(self.accum)
                                print 'new frame!'
                                self.data.put( frame.images[0].bytedata )
                                f = open(file_name, 'w')
                                f.write(message)
                                f.close
                                latestFr = frame.seq
                            else:
                                self.accum = '\n'.join((self.accum,'  frame{:#04} >> {}  |  devId: {:#02}  |  Checksum!OK'.format(latestFr+1, 'filenotstored', 0)))
                                self.console.set(self.accum)
                            read = False
        self.socket.close()
#        fmt = '  {:-^'+str(len(sep)-2)+'}\n'
#        self.accum = '\n'.join((self.accum, fmt.format('Connection terminated.')))
#        self.console.set(self.accum)
        
        
        