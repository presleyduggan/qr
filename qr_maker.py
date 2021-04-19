# simple program to generate QR codes easily and quickly

import qrcode
import os
import tkinter as tk
from tkinter import colorchooser
from qrcode.image.pure import PymagingImage
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk

class qr:
    def __init__(self, color1="white", color2="black", link="Hello"):
        # initialize variables
        self.fill_color = color1 # back
        self.back_color = color2 # fill
        self.link = link

        # initialize GUI
        self.window = tk.Tk()
        self.data_entry = tk.Entry(self.window)
        canvas = tk.Canvas(self.window, width = 400, height = 150)
        canvas.place(x=200, y=260)
        canvas.create_window(300,120,window=self.data_entry)
        self.data_entry.lift()
        self.panel = tk.Label(self.window)
        self.panel.place(x=400,y=50)
        self.window.title("Grad College QR Generator")
        self.DisplayImage()

        # initialize buttons
        ForeColorBut = tk.Button(self.window, text="Fill Color", command= self.fillColor)
        BackColorBut = tk.Button(self.window, text="Background Color", command= self.backColor)
        LinkBut = tk.Button(self.window, text="Update Link", command= self.changeLink)
        UNLVBut = tk.Button(self.window, text="Recruitment Colors", command= self.UNLVcolor)
        SaveBut = tk.Button(self.window, text="Save As", command= self.save)

        # initialize button placement
        ForeColorBut.place(x = 800, y= 400)
        BackColorBut.place(x= 100, y= 400)
        LinkBut.place(x=450, y=450)
        UNLVBut.place(x=420, y=600)
        SaveBut.place(x=700, y = 600)

        # window size and mainloop
        self.window.geometry('1000x800')
        self.window.mainloop()

    def fillColor(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        # in case color chooser is exited before a color is chosen
        if(color_code[0] == None and color_code[1] == None):
            color_code = [0,self.fill_color]
        self.fill_color = color_code[1]
        self.DisplayImage()

    def backColor(self):
        color_code = colorchooser.askcolor(title ="Choose color")
        # in case color chooser is exited before a color is chosen
        if(color_code[0] == None and color_code[1] == None):
            color_code = [0,self.back_color]
        self.back_color = color_code[1]
        self.DisplayImage()

    # DisplayImage(1) if you'd like to return the image, displays preview
    def DisplayImage(self, return_image=0):
        qr = qrcode.QRCode(version=1, error_correction= qrcode.constants.ERROR_CORRECT_L, box_size=50, border=1)
        qr.add_data(self.link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        img.save('qr2.png')
        img_original = (Image.open('qr2.png'))
        img = img_original.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel.configure(image=img)
        self.panel.image = img

        # delete that extra file
        if(os.path.exists('qr2.png')):
            os.remove('qr2.png')

        if(return_image == 1):
            return img_original

    def changeLink(self):
        x1 = self.data_entry.get()
        self.data_entry.delete(0, 'end')
        self.data_entry.insert(0, "")
        self.link = x1
        self.DisplayImage()

    def UNLVcolor(self): # colors that work well for UNLV Recruitment
        self.fill_color = 'darkgrey' #used to be 'darkred' 
        self.back_color = '#e41836'
        self.DisplayImage()

    def save(self):
        save_image = self.DisplayImage(1)
        filename = asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
            return
        save_image.save(filename)


Reader = qr()