import numpy as np
import cv2

pic=np.zeros((500,500,3),dtype='uint8')
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,'Prasad',(80,80),font,2,(255,255,255),3,cv2.LINE_8)

cv2.imshow('text',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
