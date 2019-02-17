import numpy as np
import cv2

img=cv2.imread("sha.jpg")
img=cv2.imwrite("sha.png",img)
cv2.imshow('original',img)
q=cv2.waitKey(0)
cv2.destroyAllWindows();
