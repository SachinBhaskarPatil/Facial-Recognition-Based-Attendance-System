# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
import face_recognition
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\sbpat\Documents\Python_Test_Projects\Images_GUI\banner.jpg")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=130)

        # backgorund image 
        bg1=Image.open(r"E:\python project\GUI\bg2.jpg")
        bg1=bg1.resize((1530,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        
        std_img_btn=Image.open(r"E:\python project\GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_detection,image=self.std_img1,cursor="hand2")
        std_b1.place(x=700,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_detection,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=700,y=350,width=180,height=45)



    #================face recognition==================
    def face_detection(self):

            path='images'
            images=[]
            personname=[]

            mylist=os.listdir(path)
            print(mylist)
            for curr_img in mylist:
                current_img=cv2.imread(f'{path}/{curr_img}')
                images.append(current_img)
                personname.append(os.path.splitext(curr_img)[0])
            print(personname)
            def faceencoding(images):
                encodelist=[]
                for img in images:
                    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    encode=face_recognition.face_encodings(img)[0]
                    encodelist.append(encode)
                return encodelist
            encodelistknow=(faceencoding(images))
            print("All Encodings Complete!!!")
            cap=cv2.VideoCapture(0) #here we use a laptop camera so use a 0

            def attendance(name):
                with open('attendence.csv', 'r+') as f:
                    mydatalist = f.readlines()
                    namelist = []
                    for line in mydatalist:
                        entry = line.split(',')
                        namelist.append(entry[0])
                    if name not in namelist:
                        time_now = datetime.now()
                        tStr = time_now.strftime('%H:%M:%S')
                        dStr = time_now.strftime('%d/%m/%Y')
                        f.writelines(f'\n{name},{tStr},{dStr}')

            while True:
                ret,frame=cap.read()
                faces=cv2.resize(frame,(0,0),None,0.25,0.25)
                faces=cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)

                facescurrentframe=face_recognition.face_locations(faces)

                encodescurrentframe=face_recognition.face_encodings(faces,facescurrentframe)

                for encodeface,facloc in zip(encodescurrentframe,facescurrentframe):
                    matches=face_recognition.compare_faces(encodelistknow,encodeface) 
                    facedis= face_recognition.face_distance(encodelistknow,encodeface)

                    matchindex=np.argmin(facedis)
                    if matches[matchindex]:
                        name=personname[matchindex].upper()
                        y1,x2,y2,x1=facloc
                        y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                        attendance(name)
                cv2.imshow("camera",frame)
                if cv2.waitKey(10)==13:
                    break
            cap.release()
            cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()