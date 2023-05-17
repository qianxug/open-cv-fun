import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgVec = cv.resize(cv.imread('side-by-side.jpg'), (1000, 700))[250:600, 0:1000]
imgVecHsv = cv.cvtColor(imgVec, cv.COLOR_BGR2HSV)

maskGray = cv.inRange(imgVecHsv, (5, 20, 0), (30, 200, 90))
maskCyan = cv.inRange(imgVecHsv, (0, 5, 20), (70, 60, 180))

plt.imshow(maskGray, cmap = 'gray')
plt.title('gray mask')
plt.show()

plt.imshow(maskCyan, cmap = 'gray')
plt.title('cyan mask')
plt.show()

# cv.imshow('imgVecHsv', imgVecHsv)
# cv.waitKey(0)