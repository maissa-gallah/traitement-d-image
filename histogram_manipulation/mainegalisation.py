
import numpy as np
import sys
sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")
from read_write_histogram.histogram import histogram, histogramcumul
from  read_write_histogram.readPGM import readPGM
from egalisationh import egalisation


path="D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/images/"

img , lx ,ly =readPGM(path+"cours.pgm")
heg=egalisation(img,lx,ly)
print("histogramme egalisé=")
print(heg)