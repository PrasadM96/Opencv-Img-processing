import cv2
import numpy

cap=cv2.VideoCapture('index (7).mp4')
thval1=50
thval2=100


while (cap.isOpened()):
	ret,frame=cap.read()
	canny=cv2.Canny(frame,thval1,thval2)
	cv2.imshow('Video',canny)
	
	
	if cv2.waitKey(1)==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
