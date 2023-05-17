import cv2 as cv
import numpy as np

image = cv.resize(cv.imread('IMG_3823(2).jpg'), (1200, 800))
  
# Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  
# Find Canny edges
edged = cv.Canny(gray, 30, 200)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  
cv.imshow('Canny Edges After Contouring', edged)

print("Number of Contours found = " + str(len(contours)))
  
# Draw all contours
cv.drawContours(image, contours[0:500], -1, (0, 0, 255), 3)
  
cv.imshow('Contours', image)
cv.waitKey(0)