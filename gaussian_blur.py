import cv2
import numpy

pic=cv2.imread('ronal2.jpg')

matrix=(7,7)

blur=cv2.GaussianBlur(pic,matrix,0)

cv2.imshow('Blur',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
