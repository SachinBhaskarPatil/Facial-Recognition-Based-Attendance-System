from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\sbpat\Documents\Python_Test_Projects\Images_GUI\banner.jpg")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\sbpat\Documents\Python_Test_Projects\Images_GUI\bg4.png")
        bg1=bg1.resize((1530,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"E:\python project\dev\parag.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=360,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Parag Patil",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=360,y=380,width=180,height=45)

        
        det_img_btn=Image.open(r"E:\python project\dev\sachin.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=600,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Sachin Patil",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=600,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"E:\python project\dev\sapna.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=850,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Sapana Mali",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=850,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"E:\python project\dev\ritika.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1120,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="Ritika Dhamane",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1120,y=380,width=180,height=45)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()