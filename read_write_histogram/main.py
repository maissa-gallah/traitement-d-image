
from statistics import variance
from histogram import histogram, histogramcumul
from readPGM import readpgm
from writePGM import pgmwrite
import numpy 
import math

path="D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/images/"

print(readpgm(path+"cours.pgm"))
img , lx ,ly =readpgm(path+"cours.pgm")
maxVal=img.max()
pgmwrite(img, path+"td.pgm",lx,ly)
moyenne = numpy.mean(img)
variance = numpy.var(img)
print("moyenne=",moyenne)
print("l'ecart type =",math.sqrt(moyenne))
#histogram 
h=histogram(img,lx,ly)
print("histogramme  =",h)
print("histogramme cumule  =",histogramcumul(h,maxVal))






