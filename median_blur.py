import cv2
import numpy

pic=cv2.imread('ronal3.jpeg')

kernal=3

median=cv2.medianBlur(pic,kernal)

cv2.imshow('median',median)
cv2.waitKey(0)
cv2.destroyWindows()
