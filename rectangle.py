import numpy as np
import cv2

pic = np.zeros((500,500,3),dtype='uint8')

cv2.rectangle(pic,(10,10),(50,50),(123,26,89),3,lineType=5,shift=0)

cv2.imshow('dark',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
