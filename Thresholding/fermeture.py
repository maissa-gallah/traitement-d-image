import sys
sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")
from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this


def fermeture(image_src):
    img_e = erode_this(image_src,3, with_plot=True )
    img_d = dilate_this(img_e, dilation_level=9, with_plot=True)
    return img_d