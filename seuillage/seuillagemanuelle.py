
import numpy as np

def changepixel(imgn,i,j,sb,sv,sr):
    if imgn[i][j][0]<sb:
        imgn[i][j][0]=0
    else:
        imgn[i][j][0]=255

    if imgn[i][j][1]<sv:
        imgn[i][j][1]=0
    else:
        imgn[i][j][1]=255
                
    if imgn[i][j][2]<sr:
        imgn[i][j][2]=0
    else:
        imgn[i][j][2]=255

def seuillagemanuelle(img,lx,ly,n,sr,sv,sb,et,ou):
    imgn=np.copy(img)
    # ET entre les seuils
    if(et==1):
        for i in range(lx):
            for j in range(ly):
                if imgn[i][j][0]>sb and imgn[i][j][1]>sv and imgn[i][j][2]>sr:
                    imgn[i][j]=imgn[i][j]
                else:
                    changepixel(imgn,i,j,sb,sv,sr)
     # OU entre les seuils               
    if(ou==1):
        for i in range(lx):
            for j in range(ly):
                if imgn[i][j][0]>sb or imgn[i][j][1]>sv or imgn[i][j][2]>sr:
                    imgn[i][j]=imgn[i][j]
                else:
                    changepixel(imgn,i,j,sb,sv,sr)
  
    else  :
        for i in range(lx):
            for j in range(ly):
                changepixel(imgn,i,j,sb,sv,sr)                  
    return imgn

