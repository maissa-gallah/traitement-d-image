from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from cv2 import cv2
import numpy as np
import threading
import webbrowser
import sys



sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps")

from  read_write_histogram.readPGM import readPGM
from filtre_moyen_filtre_median.bruit import bruit
from read_write_histogram.writePGM import writePGM

tk = Tk()
windowWidth = tk.winfo_reqwidth()
windowHeight = tk.winfo_reqheight()
positionRight = int(tk.winfo_screenwidth()/3 - windowWidth/3)
positionDown = int(tk.winfo_screenheight()/3 - windowHeight/1)
tk.geometry(f"800x510+{positionRight}+{positionDown}")
tk.resizable(width=False, height=False)


tk.title("Image Processing Tool")
F1 = Frame(tk)
F1.grid(row=0, column=0,pady=25, padx=25)
l1 = Label(F1, text="Original Image", font="bold")
l1.grid(row=0, column=0)
L1 = Label(F1, text="Original Image",height="25",width="52",bd=0.5, relief="solid")
L1.grid(row=1, column=0, pady=10, padx=15)
l2 = Label(F1, text="Modified Image", font="bold")
l2.grid(row=0, column=1)
L2 = Label(F1, text="Modified Image",height="25",width="52",bd=0.5, relief="solid")
L2.grid(row=1, column=1)
F2 = None
F3 = None

def add_image():
    global hsv
    global tkimage
    global original
    global img_rgb
    global selected_image
    selected_image = filedialog.askopenfilename(initialdir = "Desktop")
    # Returns If No Image Selected
    if not selected_image:
        return
    print(selected_image)

    try:
        original = cv2.imread(selected_image)
        # Open Image
        im = Image.fromarray(original)
        im.thumbnail((360, 360))
        tkimage = ImageTk.PhotoImage(im)
        img_rgb = np.array(im)

        # Parameter used when converting from RGB to BGR cv2.COLOR_RGB2BGR
        hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # Widget
        L1 = Label(F1, image = None)
        L1.config(image = tkimage)
        
        L2 = Label(F1, image = None)
        L2.config(image = tkimage)

        L1.grid(row=1, column=0)
        L2.grid(row=1, column=1)
        saveBTN.config(state="normal",cursor="hand2")
        tk.geometry("1200x510")
    except:
        return

v1 = DoubleVar()
v2 = DoubleVar()
v3 = DoubleVar()
v4 = DoubleVar()
v5 = DoubleVar()
v6 = DoubleVar()
v7 = DoubleVar()
v8 = DoubleVar()
v9 = DoubleVar()
v10 = DoubleVar()
v11 = DoubleVar()


def Record():
    # Record new image
    dosyaAdi = filedialog.asksaveasfilename(initialdir ="Desktop")
    if not dosyaAdi:
        return
    RecordMesajı = Label(F1, text="Record Done.", font="bold")
    RecordMesajı.grid(row=2, column=1,pady=27)
    RecordMesajı.after(2000, RecordMesajı.destroy)


def trgt2():
    threading.Thread(target=add_image).start()
def trgt3():
    threading.Thread(target=Record).start()

def maissa():
    img,lx,ly=readPGM(selected_image)
    imgbruit=bruit(img,lx,ly)
    imgtk3 = ImageTk.PhotoImage(image=Image.fromarray(imgbruit)) 
    L2 = Label(F1, image = imgtk3)
    L2.image = imgtk3
    L2.grid(row=1, column=1)

    
B1 = Button(tk, text = "Add Image", command=trgt2)
B1.config(cursor="hand2")
B1.place(x=180,y=450)


#hsv_btn.place(x=800,y=56)
#blur_btn.place(x=800,y=90)
#hsv_btn.place(x=800,y=124)
blur_btn = Button(tk,text="maissa", width = 13,command=maissa)
blur_btn.config(cursor="hand2")
blur_btn.place(x=800,y=158)


saveBTN = Button(tk, text = "Save Image", command=trgt3)
saveBTN.config(state="disabled")
saveBTN.place(x=565,y=450)

def callback(url):
    webbrowser.open_new(url)
me = Label(tk, text="Developers: Maissa Gallah - Chadha Siala", fg="#6E7371",cursor="hand2",font="Verdana 7 bold")
me.place(x=280,y=485)

tk.mainloop()