import sys
sys.path.append("D:/desktopMaissa/gl4/S2/Traitement d'image/TPGL4/tps/")
from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this


def ouverture(image_src):
    img_d = dilate_this(image_src, dilation_level=9, with_plot=True)
    img_e = erode_this(img_d, 3, with_plot=True)
    return img_e