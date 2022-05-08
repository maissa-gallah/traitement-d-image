import cv2 as cv
import sys
sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")

from seuillage.seuillagemanuelle import seuillagemanuelle


path="D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/images/"

img = cv.imread(path+'sign.ppm') 
cv.imshow("sans seuillage", img)


lx,ly,n=img.shape
imgseuillagemanuelleEt=seuillagemanuelle(img,lx,ly,n,50, 50, 50,1,0)
cv.imshow(" et ", imgseuillagemanuelleEt)


imgseuillagemanuelleOu=seuillagemanuelle(img,lx,ly,n,50, 50, 50,0,1)
cv.imshow(" ou ", imgseuillagemanuelleOu)

imgseuillagemanuelle=seuillagemanuelle(img,lx,ly,n,50, 50, 50,0,0)
cv.imshow(" manuelle ",imgseuillagemanuelle)




cv.waitKey()