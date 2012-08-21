#!/usr/bin/env python
from teledroid import TCP, UDP, IP
import Tkinter as tk
import threading
import Queue
import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk



UDPport = 50050
TCPport = 60000
sender = TCP.TCPserver(TCPport)
indata = UDP.UDPread(UDPport, IP.getBroadcast())
 
class tkGUI:
    def __init__(self, root):
        self.connect = tk.Button(root, text='Connect', command=self.connectTCP, width=10)
        self.snap = tk.Button(root, text='Grab Image', command=self.grabImage, width=10, state=tk.DISABLED)
        self.qu   = tk.Button(root, text='Quit', command=self.endTCP, width=10, state=tk.DISABLED)
        self.console = tk.Label(root, anchor = 'nw',font=('Courier 10 Pitch', '11'), fg = "white", bg = "black", width = 60, height = 19)
        self.showData = tk.Label(root, anchor = 'w',font=('Courier 10 Pitch', '11'), fg = "orange", bg = "black", width = 30, height = 7, justify='left')
        self.showMatrix = tk.Label(root, anchor = 'nw',font=('Courier 10 Pitch', '11'), fg = "orange", bg = "black", width = 30, height = 7, justify='left')
        self.photo = tk.PhotoImage(file="init.pgm")
        self.image = tk.Label(root, image=self.photo, borderwidth=3)
        self.image.photo = self.photo
        
        self.connect.grid(row=0, column=0)
        self.snap.grid(row=0, column=1)
        self.qu.grid(row=0, column=2)
        self.image.grid(rowspan=2, row=1,columnspan=3, padx=7, pady=5)
        self.console.grid(columnspan=2, rowspan=1,row=1, column=3, pady=2, padx=(0, 7))
        self.showData.grid(row=2,column=3,pady=2)
        self.showMatrix.grid(row=2,column=4, pady=2, padx=(2, 7))
        
        self.root = root
        self.displayThread = threading.Thread(target=self.waitConnection)
        self.go = True
        
    def connectTCP(self):
        sender.start()
        self.connect.config(text = 'Awaiting...')
        self.connect.config(state = tk.DISABLED)
        self.connect.config(relief=tk.SUNKEN)
        self.displayThread.start()
    
    def waitConnection(self):
        # runs on a sepparate thread
        while self.go:
            if sender.ready:
                indata.go(self.root)      # start the UDP reception thread
                self.console.config(textvariable = indata.console, )
                self.showData.config(textvariable = indata.showData)
                self.showMatrix.config(textvariable = indata.showMat)
                break
        self.connect.config(text = 'Connected!')
        self.connect.config(relief=tk.FLAT)
        self.snap.config(state = tk.NORMAL)
        self.qu.config(state = tk.NORMAL)
        # image handling
        while self.go:
            #grab jpegs from queue and diplay them
            try:
                rawstring = indata.data.get_nowait()
                imageNp = np.fromstring(rawstring, dtype='uint8')
                imgecv = cv2.imdecode(imageNp, 0) # opencv used only for this reason JPEG -> raw
                pi = Image.fromarray(imgecv)
                photo = ImageTk.PhotoImage(pi)
                self.image.config(image = photo)
                self.image.photo = photo
            except Queue.Empty:
                pass
            
    def grabImage(self):
        sender.sendSnap()
        
    def endTCP(self):
        sender.sendQuit()
        indata.endthis = True
        self.go = False
        alldone = False
        while not (alldone): # check if all socketes are closed and threads are finished 
            alldone = sender.finished and indata.finished and not self.displayThread.isAlive()
        self.root.quit()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Android Protobuff Server')
    root.iconbitmap(bitmap='@pixlogo.xbm')   
    app = tkGUI(root)
    root.mainloop()
    
    
    