
from tkinter import messagebox
import cv2 as cv
import numpy as np
import sys



sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")

from Thresholding.manual_thresholding import manual_threshholding

import tkinter
from tkinter import filedialog

def filePath():
    #initiate tinker and hide window 
    main_win = tkinter.Tk() 
    main_win.withdraw()

    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')

    main_win.deiconify()
    main_win.lift()
    main_win.focus_force()

    #open file selector 
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/",
    title='Please select a directory')

    #close window after selection 
    main_win.destroy()

    #print path 
    return main_win.sourceFile





top = tkinter.Tk()
def helloCallBack(): 
    a=filePath()
    print( a)
    img = cv.imread(a) 
    cv.imshow("M Th", img)

def helloCallBack2222222222222222(): 
    a=filePath()
    print( a)
    img = cv.imread(a) 
    cv.imshow("landscape", img)
    new_img = manual_threshholding(img, 150, 150, 150)
    cv.imshow("M Th", new_img)
   

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()