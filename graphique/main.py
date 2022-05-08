import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np


def select_image():

    global img

    path = filedialog.askopenfilename()


    if path:
    
        img = cv2.imread(path, cv2.COLOR_BGR2RGB)
        grayScale = ''
        
        image = Image.fromarray(img)
        image_tk = ImageTk.PhotoImage(image)


        if vargray.get() == 1:
            grayScale = cv2.imread(path, 0)  
            grayScale_img = Image.fromarray(grayScale)
            grayScale_img_tk = ImageTk.PhotoImage(grayScale_img)

            panelDST.configure(image=grayScale_img_tk)
            panelDST.image = grayScale_img_tk 
        
        panelSRC.configure(image=image_tk)
        panelSRC.image = image_tk
    
        

def rotate_left():
    global img

    if img.any():  #check whether image exists
        
        image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

        img = image
        
        image = Image.fromarray(image)
        image_tk = ImageTk.PhotoImage(image)

        panelSRC.configure(image=image_tk)
        panelSRC.image = image_tk


def rotate_right():
    global img
    if img.any():
        
        image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        img = image
        
        image = Image.fromarray(image)
        image_tk = ImageTk.PhotoImage(image)

        panelSRC.configure(image=image_tk)
        panelSRC.image = image_tk


root = tk.Tk()
root.title('toolbox')  # window title is toolbox


img = np.array([])  # set it to numpy array initially

vargray = tk.IntVar()
chkbtn = tk.Checkbutton(root, text="gray?", variable=vargray)
chkbtn.pack()

w = tk.Label(root, text="Hi, Welcome to Zeiad's toolbox !")
w.pack()

btn = tk.Button(root, text="Select an image", command=select_image)
btn1= tk.Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="y", expand="yes", padx="10", pady="10")
btn1.pack(side="bottom", fill="y", expand="yes", padx="20", pady="20")

rotclk = tk.Button(root, text="RotRight", command=rotate_right)
rotclk.pack(side='right')

rokanticlk = tk.Button(root, text='RotLeft', command=rotate_left)
rokanticlk.pack(side='left')

brightup = tk.Button(root, text="RotLeft", command="buttonpressed")
brightdown = tk.Button(root, text="RotLeft", command="buttonpressed")

Exit1 = tk.Button(root, text="Exit", command=root.destroy)

btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
Exit1.pack(side='bottom')

panelSRC = tk.Label(root)
panelSRC.pack(side="left", padx=10, pady=10)

panelDST = tk.Label(root)
panelDST.pack(side="right", padx=10, pady=10)

root.mainloop() 