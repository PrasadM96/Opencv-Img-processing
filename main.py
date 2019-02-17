# import the OpenCV package
import cv2
 
# load the image with imread()
imageSource = 'sha.jpg'
image = cv2.imread(imageSource)
 
# display the image on screen with imshow()
# after checking that it loaded
if image is not None:
    cv2.namedWindow( 'Display window', cv2.WINDOW_AUTOSIZE );
    cv2.imshow('Display window',image)
elif image is None:
    print ("Could not open or find the image")
 
# wait time in milliseconds
# this is required to show the image
# 0 = wait indefinitely
k = cv2.waitKey(0)
 
# destroy the window
cv2.destroyAllWindows()
