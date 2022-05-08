

import cv2 as cv
import numpy as np
import sys



sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")

from Thresholding.ouverture import ouverture
from Thresholding.fermeture import fermeture
from read_write_histogram.writePGM import pgmwrite
from Thresholding.manual_thresholding import manual_threshholding
from Thresholding.auto_threshholding import otsu
from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this
from read_write_histogram.readPGM import readpgm


path="D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/images/"

#---------------------------------------------------------- Manual threshholding
img = cv.imread(path+'snail.ppm') 
cv.imshow("landscape", img)
new_img = manual_threshholding(img, 150, 150, 150)
cv.imshow("M Th", new_img)

#new_img_and = manual_threshholding(img, 150,150,150,"AND")
#cv.imshow("M Th AND", new_img_and)

#new_img_or = manual_threshholding(img, 100,150,150,"OR")
#cv.imshow("M Th OR", new_img_or)

#---------------------------------------------------------- Auto threshholding
[th0, th1, th2] = otsu(img)
print(th0," ", th1," ", th2) # 129   142   162
img2 = manual_threshholding(img, th2, th1, th0 )
cv.imshow("tesssst", img2)

#---------------------------------------------------------- Dilatation
image_src, lx, ly = readpgm(path+'coins.pgm')

image_org = cv.imread(path+ "coins.pgm") 
cv.imshow("image source", image_org)

img_d = dilate_this(image_src, dilation_level=9, with_plot=True)
pgmwrite(img_d, path+ "dilated.pgm",lx,ly,"P2")
dilated = cv.imread(path+ "dilated.pgm") 
cv.imshow("dilated.pgm", dilated)

#---------------------------------------------------------- erosion
img_e = erode_this(image_src, 3, with_plot=True)
pgmwrite(img_e, path+ "erosion.pgm",lx,ly,"P2")
erosion = cv.imread(path+ "erosion.pgm") 
cv.imshow("erosion.pgm", erosion)

#---------------------------------------------------------- ouverture
imgo = ouverture(image_src)
pgmwrite(imgo, path+ "ouverture.pgm",lx,ly,"P2")
imgouverture = cv.imread(path+ "ouverture.pgm") 
cv.imshow("ouverture.pgm", imgouverture)

#---------------------------------------------------------- fermeture
imgf=fermeture(image_src)
pgmwrite(imgf, path+ "fermeture.pgm",lx,ly,"P2")
imgfermeture = cv.imread(path+ "fermeture.pgm") 
cv.imshow("fermeture.pgm", imgfermeture)

cv.waitKey()