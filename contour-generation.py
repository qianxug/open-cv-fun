import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='for generating contours and evaluating contour density')
parser.add_argument('--input', type=str, help='path to a photo', default="assets\side-by-side.jpg")

args = parser.parse_args()

image = cv.GaussianBlur(cv.resize(cv.imread(args.input), (1200, 800)), (5, 5), 0)
  
# Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv.Canny(gray, 30, 200)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# cv.imshow("Original image", image)
# cv.imshow('Canny Edges After Contouring', edged)

print("Number of Contours found = " + str(len(contours)))
  
# Draw all contours
cv.drawContours(image, contours, -1, (255, 255, 0), 2)

region1 = image[355:450, 95:595]
region2 = image[355:450, 635:1135]

# region1
for slot in range(5):
    slotContourDensity = 0

    for i in range(95):
        for j in range(100):
            b, g, r = image[355 + i][95 + 100 * slot + j]
            if (b, g, r) == (255, 255, 0):
                slotContourDensity += 1
    
    print('for the right rack, the contour density of slot', slot + 1, "is", slotContourDensity)

for slot in range(5):
    slotContourDensity = 0

    for i in range(95):
        for j in range(100):
            b, g, r = image[355 + i][635 + 100 * slot + j]
            if (b, g, r) == (255, 255, 0):
                slotContourDensity += 1
    
    print('for the left rack, the contour density of slot', slot + 1, "is", slotContourDensity)

cv.rectangle(image, (95, 355), (195, 450), (0, 255, 0), 2)
cv.rectangle(image, (195, 355), (295, 450), (0, 255, 0), 2)
cv.rectangle(image, (295, 355), (395, 450), (0, 255, 0), 2)
cv.rectangle(image, (395, 355), (495, 450), (0, 255, 0), 2)
cv.rectangle(image, (495, 355), (595, 450), (0, 0, 255), 2)

cv.rectangle(image, (635, 355), (735, 450), (0, 0, 255), 2)
cv.rectangle(image, (735, 355), (835, 450), (0, 0, 255), 2)
cv.rectangle(image, (835, 355), (935, 450), (0, 0, 255), 2)
cv.rectangle(image, (935, 355), (1035, 450), (0, 0, 255), 2)
cv.rectangle(image, (1035, 355), (1135, 450), (0, 0, 255), 2)

cv.imshow("4/5 full rack", region1)
cv.imshow("empty rack", region2)
cv.waitKey(0)