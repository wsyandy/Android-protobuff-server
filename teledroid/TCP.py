#!/usr/bin/env python
'''
Created on Aug 8, 2012

@author: Federico Camoposeco
'''

import threading
import socket

'''
    Simple class to send a TCP message to the phone in order to remotely
    start and stop the data logging (or take snapshots). For the moment
    only snapshots are supported. Methods are threaded in order to be 
    reliably used as Tkinter button commands.
'''

class TCPserver(threading.Thread):
    '''
    Threaded class to handle the commands to be sent to the android 
    logging utility. PORT should be a non restricted port (>50000),
    usage: TCPserver(PORT, HOST='0.0.0.0')
    
    '''
    def __init__(self, PORT, HOST=''):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)
        self.ready = False
        self.finished = True
        
    def run(self):
        self.pipe, _ = self.socket.accept()
        self.finished = False
        self.ready = True
        
    def sendSnap(self):
        t = threading.Thread(target=self.pipe.send, args=('snap\n', ))
        t.start()
        t.join()
    
    def sendQuit(self):
        t = threading.Thread(target=self.pipe.send, args=('q\n', ))
        t.start()
        t.join()
        self.stop()
        
    def stop(self):
        self.socket.close()
        self.pipe.close()
        self.finished = True
        

        