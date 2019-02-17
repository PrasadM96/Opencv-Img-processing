import cv2
import numpy

img =cv2.imread('pra.jpg',0)

threshold_value=95
(T_value,binary_threshold)=cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow('BINARY',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
