
import cv2 as cv
import sys


sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")

from filtre_moyen_filtre_median.bruit import bruit
from read_write_histogram.writePGM import pgmwrite
from  read_write_histogram.readPGM import readpgm
from filtre_moyen_filtre_median.filtre import moyennefilter
path="D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/images/"

img1 = cv.imread(path+'example.pgm') 
cv.imshow("Test", img1)
img,lx,ly=readpgm(path+'example.pgm')
imgb=bruit(img,lx,ly)

pgmwrite(imgb, path+"bruit.pgm",lx,ly)
imgbruit = cv.imread(path+"bruit.pgm") 
cv.imshow("bruit.pgm", imgbruit)

imgm=moyennefilter(img,lx,ly,5)
pgmwrite(imgm, path+"filtermoyenne.pgm",lx,ly)
imgfiltermoy = cv.imread(path+"filtermoyenne.pgm") 
cv.imshow("filtermoyenne.pgm", imgfiltermoy)


cv.waitKey()