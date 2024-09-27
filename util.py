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


def remove_noise(img, ksize=5):
    return cv2.medianBlur(img, ksize)


# dilation
def dilate(image, iterations=1):
    kernel = np.ones((2, 2), np.uint8)
    return cv2.dilate(image, kernel)


# erosion
def erode(image, iterations=1):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def save_img(filename, im):
    cv2.imwrite(filename, im)


def show_img(title, im):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 800, 600)
    cv2.imshow(title, im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_text(img):
    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    pytesseract.image_to_string(img, config=custom_config)
    return pytesseract.image_to_string(img)
    # return pytesseract.image_to_data(img, output_type=Output.DICT)
