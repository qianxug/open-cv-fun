from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()

else:
    backSub = cv.createBackgroundSubtractorKNN()

capture = cv.imread(args.input)
fgMask = backSub.apply(capture)
    
cv.rectangle(capture, (10, 2), (100,20), (255,255,255), -1)

cv.imshow('capture', capture)
cv.imshow('FG Mask', fgMask)

cv.waitKey()