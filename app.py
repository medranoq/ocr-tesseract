import cv2
import numpy as np

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#thresholding
def get_thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)[1]

#opening - erosion followed by dilation
def get_opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def get_canny(image):
    return cv2.Canny(image, 100, 200)

im = cv2.imread('img/py_logo.png') #función para cargar la imágen

im_gray = get_grayscale(im)

im_thr_bin = get_thresholding(im_gray)

im_op = get_opening(im_gray)

im_canny = get_canny(im_gray)

print(im.shape)
print(im_gray.shape)
print(im_thr_bin.shape)
print(im_op.shape)

#guardar imágen
cv2.imwrite('img/py_gray_logo.png', im_gray)
cv2.imwrite('img/py_thr_bin_logo.png',im_thr_bin)
cv2.imwrite('img/py_open_logo.png',im_op)
cv2.imwrite('img/py_canny_logo.png',im_canny)

