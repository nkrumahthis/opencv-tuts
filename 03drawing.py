import numpy as np
import cv2

img = cv2.imread('stuff/bennetterica.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150, 150), (255,0,0), 15)
cv2.rectangle(img, (15,25), (200,150), 5)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()