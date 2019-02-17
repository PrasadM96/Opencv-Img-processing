import cv2
import numpy as np

img=cv2.imread('sha.png')
cols=img.shape[1]
rows=img.shape[0]

M=np.float32([[1,0,-150],[0,1,-70]])
shifted_one=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Shifted',shifted_one)
#cv2.imshow('original',img)
cv2.waitKey(0)
cv2.detroyAllWindows()
