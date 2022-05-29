
from statistics import variance
from histogram import histogram, histogramcumul
from readPGM import readPGM
from writePGM import writePGM
import numpy 
import math

path="C:/Users/LENOVO/Desktop/my python/traitement-d-image/images/"

print(readPGM(path+"cours.pgm"))
img , lx ,ly =readPGM(path+"cours.pgm")
maxVal=img.max()
writePGM(img, path+"td.pgm",lx,ly, "P2")
moyenne = numpy.mean(img)
variance = numpy.var(img)
print("moyenne=",moyenne)
print("l'ecart type =",math.sqrt(moyenne))
#histogram 
h=histogram(img,lx,ly)
print("histogramme  =",h)
print("histogramme cumule  =",histogramcumul(h,maxVal))






