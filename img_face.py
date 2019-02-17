import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

pic=cv2.imread('binary.png')
scale_factor=1.3

while 1:
	faces=face_cascade.detectMultiScale(pic,scale_factor,5)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
		
		cv2.imshow('ImgDetect',pic)
		
	if cv2.waitKey(1)==ord('q'):
			break
			
cv2.destroyAllWindows()
