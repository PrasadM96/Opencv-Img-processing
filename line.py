import numpy as np
import cv2

pic=np.zeros((250,250,3),dtype='uint8')
cv2.line(pic,(0,0),(250,250),(255,0,255))
cv2.line(pic,(250,0),(0,250),(255,0,255))
cv2.imshow('line_drawing',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
