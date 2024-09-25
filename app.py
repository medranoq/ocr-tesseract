from os import remove

import cv2
import numpy as np
import pytesseract
from pytesseract import Output


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# thresholding
def get_thresholding(image):
    return cv2.threshold(image, 40, 200, cv2.THRESH_BINARY)[1]


# opening - erosion followed by dilation
def get_opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def get_canny(image):
    return cv2.Canny(image, 100, 200)


def remove_noise(image):
    return cv2.medianBlur(image, 7)


# dilation
def dilate(image):
    kernel = np.ones((2, 2), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=4)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def save_img(filename, im):
    cv2.imwrite(filename, im)


def get_text(img):
    return pytesseract.image_to_data(img, output_type=Output.DICT)


im = cv2.imread('img/recorte.jpg')  # función para cargar la imágen

im_gray = get_grayscale(im)

noise = remove_noise(im_gray)

save_img('erode_binary.jpg',get_thresholding(noise))

d = get_text(get_thresholding(noise))

print(d['text'])
