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
        self.console = tk.Label(root, anchor = 'nw',font=('Courier 10 Pitch', '11'), fg = "white", bg = "black", width = 62, height = 20)
        self.photo = tk.PhotoImage(file="init.pgm")
        self.image = tk.Label(root, image=self.photo, borderwidth=3)
        self.image.photo = self.photo
        
        self.connect.grid(row=0, column=0)
        self.snap.grid(row=0, column=1)
        self.qu.grid(row=0, column=2)
        self.image.grid(row=1,columnspan=3, padx=5, pady=5)
        self.console.grid(rowspan=2,row=0, column=3, padx=3, pady=3)
        self.root = root
        self.go = True
        
    def connectTCP(self):
        sender.start()
        self.connect.config(text = 'Awaiting...')
        self.connect.config(state = tk.DISABLED)
        self.connect.config(relief=tk.SUNKEN)
        threading.Thread(target=self.waitConnection).start()
    
    def waitConnection(self):
        while self.go:
            if sender.ready:
                indata.go(self.root)      # start the UDP reception thread
                self.console.config(textvariable = indata.console)
                break
        self.connect.config(text = 'Connected!')
        self.connect.config(relief=tk.FLAT)
        self.snap.config(state = tk.NORMAL)
        self.qu.config(state = tk.NORMAL)
        # image handling
        while self.go:
            #grab jpegs from queue and diplay them
            try:
                rawstring = indata.data.get(True, 100)
            except Queue.Empty:
                pass
            imageNp = np.fromstring(rawstring, dtype='uint8')
            imgecv = cv2.imdecode(imageNp, -1) # opencv used only for this reason JPEG -> raw
            pi = Image.fromarray(imgecv)
            photo = ImageTk.PhotoImage(pi)
            self.image.config(image = photo)
            self.image.photo = photo
            print pi.size
            
            
    def grabImage(self):
        sender.sendSnap()
        
    def endTCP(self):
        sender.sendQuit()
        indata.endthis = True
        self.go = False
        self.root.after(350, self.root.quit) # wait for all threads to stop


if __name__ == '__main__':
    root = tk.Tk()      
    app = tkGUI(root)
    root.mainloop()
