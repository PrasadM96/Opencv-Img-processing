import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
scale_factor=1.3

while 1:
	ret,pic=cap.read()
	
	faces=face_cascade.detectMultiScale(pic,scale_factor,5)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(pic,(x,y),(x+w,y+w),(255,0,0),3)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(pic,'Me',(x,y),font,2,(255,255,255),2,cv2.LINE_AA)
		
	print("Number of faces found {} ",format(len(faces)))
	cv2.imshow('face',pic)
	if cv2.waitKey(1)==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()	
