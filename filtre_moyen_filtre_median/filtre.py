import numpy as np
def remplirbourdureimg(img,lx,ly,n):
    imgb =img
    a=n//2
    t=np.zeros((ly+n-1,lx+n-1))
    t[a:ly+a , a:lx+a]=img
    # padding mirror top
    t[0:a, a:a+lx] = np.flip(img[1:a+1, 0:lx],axis=0)
    # padding mirror bottom
    t[ly+a:ly+2*a, a:lx+a]= np.flip(img[ly-a-1:ly-1, 0:lx],axis=0)
    # padding mirror left
    t[:, 0:a] = np.flip(t[:, a+1:2*a+1],axis=1)
    # padding mirror right
    t[:, lx+a:lx+2*a] =  np.flip(t[:, lx-1:lx+a-1],axis=1)
    return t
  
def moyennefilter(img,lx,ly,n):
    t =remplirbourdureimg(img,lx,ly,n)
    a=n//2
    imgm=img
    new_img=img
    for i in range (a,ly+a):
        for j in range(a,lx+a):
            arr=t[i-a:i+a+1,j-a:j+a+1]
            imgm[i-a][j-a]=np.average(arr)
    return imgm

def medianFiltre(img, lx, ly, n):
    new_img = img
    a= n//2
    img_filled = remplirbourdureimg(img, lx, ly, n)

    for i in range (a, ly+a):
        for j in range(a, lx+a):
            arr=img_filled[i-a:i+a+1,j-a:j+a+1]
            print(i, ",",j)
            new_img[i-a][j-a] = np.median(arr)
    return new_img




