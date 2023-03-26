from tkinter import*
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk
import tkinter.messagebox
import os
from base64 import encode
import cv2
from face import Face_Recognition
import numpy as np
from logging import root
import face_recognition
import os
from datetime import datetime
from developer import Developer
 

class face_recognition_system:
    def __init__(self,root):
        self.root=root;
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # first image
        img1=Image.open(r"E:\python project\GUI\rcpit.jpg")
        img1=img1.resize((500,300),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=150)
         # second image
        img2=Image.open(r"E:\python project\GUI\front.png")
        img2=img2.resize((500,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=550,height=150)
         # third image
        img3=Image.open(r"E:\python project\GUI\rcpit.jpg")
        img3=img3.resize((500,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=150)
        # bg image
        img4=Image.open(r"E:\python project\GUI\bg.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1530,height=710)
        #title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        #student details button
        img5=Image.open(r"E:\python project\GUI\student.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.open_img,cursor="hand2")
        b1.place(x=200,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Student Database",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=400,width=220,height=40)
        #detect face button
        img6=Image.open(r"E:\python project\GUI\detection.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.face,cursor="hand2")
        b1.place(x=500,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=400,width=220,height=40)

        #developer button
        img11=Image.open(r"E:\python project\GUI\developer.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",command=self.developr,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=400,width=220,height=40)
        #Exit button
        img12=Image.open(r"E:\python project\GUI\exit.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,command=self.iExit,cursor="hand2")
        b1.place(x=1100,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=400,width=220,height=40)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    def open_img(self):
        os.startfile(r"E:\python project\images")

    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def face(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)



if __name__=="__main__":
    root=Tk()     
    obj=face_recognition_system(root)
    root.mainloop()

