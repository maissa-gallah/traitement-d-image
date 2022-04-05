import cv2 as cv
import sys
sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")
from  read_write_histogram.readPGM import readpgm
from read_write_histogram.writePGM import pgmwrite
from modificationcontraste import contraste

path="D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/images/"


img1 = cv.imread(path+'example.pgm') 
cv.imshow("Test", img1)

img,lx,ly=readpgm(path+'example.pgm')

imgclair=contraste(img,lx,ly,[70,50],[120,100])
pgmwrite(imgclair, path+ "dilatationzoneclair.pgm",lx,ly)
imgclair = cv.imread(path+ "dilatationzoneclair.pgm") 
cv.imshow("dilatationzoneclair.pgm", imgclair)

imgsombre=contraste(img,lx,ly,[50,200],[200,240])
pgmwrite(imgsombre, path+"dilatationzonesombre.pgm",lx,ly)
imgsombre = cv.imread(path+"dilatationzonesombre.pgm") 
cv.imshow("dilatationzonesombre.pgm", imgsombre)

imgmilieu=contraste(img,lx,ly,[50,200],[200,240])
pgmwrite(imgsombre, path+ "dilatationzonesmilieu.pgm",lx,ly)
imgmilieu = cv.imread(path+"dilatationzonemilieu.pgm") 
cv.imshow("dilatationzonemilieu.pgm", imgsombre)

imginverse=contraste(img,lx,ly,[1,255],[254,0])
pgmwrite(imginverse, path+ "inversionimage.pgm",lx,ly)
imginverse = cv.imread(path+ "inversionimage.pgm") 
cv.imshow("inversionimage.pgm", imginverse)

cv.waitKey()