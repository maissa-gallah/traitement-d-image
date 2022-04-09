import random


def bruit(img,lx,ly):
  imgb =img
  for i in range (ly):
        for j in range (lx):
            c=random.randint(0, 20)
            if c==0:
              imgb[i][j]=0
            elif c==20 :
              imgb[i][j]=255 
  return imgb 
