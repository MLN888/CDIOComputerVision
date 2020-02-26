
####################################################
#          Test for tennisball collectror          #
#                                                  #
# version 1.0                                      #
# description: A test version for visual feedback  #
#              circle and color reconition.        #
#												   #
# auther:       Phillip Bomholtz                   #
# created:      26-02-2020						   #
# last updated: 26-02-2020						   #
#												   #
####################################################


import cv2
import numpy as np 

cap = cv2.VideoCapture(1);  #setup video capture

#set resolution to 1920x1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);

#loop for displaying frames
while(True):
	ret, frame = cap.read() #read from camera and store
	lul = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #greyscale
	lul2 = cv2.blur(lul, (3, 3)) 
	detected_circles = cv2.HoughCircles(lul2,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) #look for circles

	#if any circles
	if detected_circles is not None:
		detected_circles = np.uint16(np.around(detected_circles))

		#for all cirlces
		for pt in detected_circles[0, :]:

			a, b, r = pt[0], pt[1], pt[2]  #circle coordinates
			cv2.circle(frame, (a, b), r+10, (0, 255, 255), 2)  #draw area around with radius r
			cv2.circle(frame, (a, b), 1, (100, 0, 100), 3)  #draw dot im middle

	cv2.imshow('frame',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	continue

cap.release()
cv2.destroyAllWindows()