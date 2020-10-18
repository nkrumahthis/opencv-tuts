import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('stuff/bennetterica.jpg', cv.IMREAD_GRAYSCALE)
vid = cv.imread('stuff/dexttut.mp4', cv.IMREAD_GRAYSCALE)


# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([5,100], [100,5], 'c', linewidth=2)
# plt.show()

# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()