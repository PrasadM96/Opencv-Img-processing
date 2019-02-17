import numpy  as np
import cv2

img=np.zeros((250,250,3),dtype='uint8')
color=(0,0,255)
cv2.circle(img,(125,125),100,color)
cv2.circle(img,(125,125),80,color)
cv2.imshow('circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
