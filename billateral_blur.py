import cv2
import numpy

img=cv2.imread('ronal3.jpeg')

dimpixel=7
color=100
space=100

filterr=cv2.bilateralFilter(img,dimpixel,color,space)
cv2.imshow('Filter',filterr)
cv2.waitKey(0)
cv2.destroyAllWindows()
