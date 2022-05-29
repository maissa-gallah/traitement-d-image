import numpy as np
import sys
sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")

from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this

def fermeture(img, level=3):
    img_d = dilate_this(img, dilation_level=level)
    img_e = erode_this(img_d, erosion_level=level)
    return img_e