import cv2 as cv
import numpy as np
import argparse
import os
from skimage.metrics import structural_similarity

def computePixelMSE(img1, img2):
    height1, width1 = img1.shape
    height2, width2 = img2.shape

    assert height1 == height2 and width1 == width2

    diff = cv.subtract(img1, img2)
    err = np.sum(diff**2)

    return err / float( height1 * width1)

def avgArr(arr):
    sum = 0
    
    for each in arr:
        sum += each
    
    return sum / 4

parser = argparse.ArgumentParser(description='for finding if consecutive frames are the same in a video')

parser.add_argument('--input', type=str, help='path to a video')

args = parser.parse_args()

video = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))

if not video.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)

pastFiveFrames = []

index = 0
numFrames = 0

while True:
    ret, frame = video.read()
    
    if frame is None:
        break
    
    if numFrames % 20 == 0:
        filePath = os.path.join('frames', f'image{index}.jpg')
        frame = cv.GaussianBlur(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), (7, 7), 0)

        cv.imwrite(filePath, frame)

        index += 1

        if len(pastFiveFrames) == 5:
            pastFiveFrames.pop(0)  
        
        pastFiveFrames.append(frame)

        if len(pastFiveFrames) == 5:
            SSIMs = []
            pixelDiffs = []
            
            for i in range(4):
                score, diff = structural_similarity(pastFiveFrames[i], pastFiveFrames[i + 1], full = True)
                SSIMs.append(score)

                currDiffByPixel = computePixelMSE(pastFiveFrames[i], pastFiveFrames[i + 1])
                pixelDiffs.append(currDiffByPixel)
                
            print('average SSIM score from frame{} to frame{} is {}'.format(index - 5, index, round(avgArr(SSIMs), 3)))
            print('average pixel-wise colour difference (MSE) from frame{} to frame{} is {}'.format(index - 5, index, round(avgArr(pixelDiffs), 3)))
            print('-' * 50)

    numFrames += 1

video.release()
cv.destroyAllWindows()