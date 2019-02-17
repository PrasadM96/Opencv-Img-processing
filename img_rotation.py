import numpy as np
import cv2

img=cv2.imread('sha.jpg')
rows=img.shape[1]
cols=img.shape[0]
center=(cols/2,rows/2)
angle=45

M=cv2.getRotationMatrix2D(center,angle,1)
rotated=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('rotated',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
