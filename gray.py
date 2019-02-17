import cv2
import numpy

img=cv2.imread('pra.jpg',0)
cv2.imshow('Gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
