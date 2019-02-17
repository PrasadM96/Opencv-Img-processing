import cv2
import numpy

cap=cv2.VideoCapture('index (7).mp4')
fourcc=cv2.VideoWriter_fourcc(*'XVID')
fps=30
framesize=(720,480)
out=cv2.VideoWriter('index (7).avi',fourcc,fps,framesize)
while (cap.isOpened()):
	ret,frame=cap.read()
	cv2.imshow('Video',frame)
	
	if cv2.waitKey(1)==ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
