import numpy as np
import cv2 as cv
from skimage.metrics import structural_similarity
from PIL import Image

def numPixels(filepath):
    width, height = Image.open(filepath).size
    return width * height

first = cv.imread('img1.png')
second = cv.imread('img2.png')
third = cv.imread('left.jpg')
fourth = cv.imread('STD.jpg')

first_gray = cv.cvtColor(first, cv.COLOR_BGR2GRAY)
second_gray = cv.cvtColor(second, cv.COLOR_BGR2GRAY)
third_gray = cv.cvtColor(third, cv.COLOR_BGR2GRAY)
fourth_gray = cv.cvtColor(fourth, cv.COLOR_BGR2GRAY)

score1, diff1 = structural_similarity(first_gray, second_gray, full = True)
print("SSIM Similarity Score: {:.3f}%".format(score1 * 100))

score2, diff2 = structural_similarity(third_gray, fourth_gray, full = True)
print("SSIM Similarity Score: {:.3f}%".format(score2 * 100))

score3, diff3 = structural_similarity(first_gray, third_gray, full = True)
print("SSIM Similarity Score: {:.3f}%".format(score3 * 100))



# diff2 = np.sum(np.abs(first - second))
# diff3 = np.sum(np.abs(first - first))
# print(diff2)
# print(diff3)
# print(numPixels('img1.png'))
# print(numPixels('img2.png'))
# print("Absolute Frame Difference Score: {:.3f}%".format(diff2 / numPixels('img1.png') * 100))