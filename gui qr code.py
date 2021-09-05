from tkinter import *
from tkinter import messagebox
import pyqrcode
import os
window = Tk()
window.title("QR Code generator")
def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr=pyqrcode.create(subject.get)
        qrImage=myQr.xbm(scale=6)
        global photo
        photo=BitmapImage(data=qrImage)
        else:
            messagebox.showinfo("Error","please Enter the subject")
        try:
            showCode()
        except:
            pass
def showCode():
    global photo
            

