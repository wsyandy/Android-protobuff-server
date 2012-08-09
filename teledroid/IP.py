#!/usr/bin/env python
'''
Created on Aug 8, 2012

@author: Federico Camoposeco
'''

import socket

def getLocal():
    '''
        Assumes internet non-proxy connection available.
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("gmail.com",80))
        return s.getsockname()[0]
        s.close()
    except:
        print 'You need connection to the internet!'
        return ''

def getBroadcast():
    local = getLocal()
    tokens = local.split('.')[0:3]
    return '.'.join(tokens)+'.255'
    