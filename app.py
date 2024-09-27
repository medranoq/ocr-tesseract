import cv2
from util import *

im = cv2.imread('img/gcp_ocr.png')
txt = get_text(im)
print(txt)
