
####################################################
#          Test for tennisball collectror          #
#                                                  #
# version 1.1                                      #
# description: A test version for visual feedback  #
#              circle and color reconition.        #
#												   #
# auther:       Phillip Bomholtz                   #
# created:      26-02-2020						   #
# last updated: 04-03-2020						   #
#												   #
####################################################


import cv2
import numpy as np 
import os

cap = cv2.VideoCapture(1);  #setup video capture

#set resolution to 1920x1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);

#loop for displaying frames
while(True):
    ret, frame = cap.read() #read from camera and store
    flem = cv2.imread(os.path.abspath("Circle_and_color_detection_test/Test_field_foto.jpg"),1)


    #lul = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #greyscale
    #lul2 = cv2.blur(lul, (3, 3)) 
    #detected_circles = cv2.HoughCircles(lul2, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40) #look for circles

    hsv = cv2.cvtColor(flem, cv2.COLOR_BGR2HSV)   #converte rgb to hvs
    lower = np.array([0,220,200])              #set lover accept boundury
    upper = np.array([10,255,255])            #set higher accept boundury
    mask = cv2.inRange(hsv, lower, upper)    #make mask of boundurys
    res = cv2.bitwise_and(flem,flem, mask= mask) #get only desired color

    rgb = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    grayed = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    contours,_ = cv2.findContours(grayed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #reletevistic characteristics for coordinate estimation. Subject to change!
    x_rel = 0.028 
    y_rel = 0.026
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        start_point_x = x+(w*x_rel)
        start_point_y = y+(h*y_rel)
        end_point_x = start_point_x + (w-(w*x_rel)*2)
        end_point_y = start_point_y + (h-(h*y_rel)*2)
        cv2.rectangle(flem, (int(start_point_x),int(start_point_y)), (int(end_point_x),int(end_point_y)), (0,255,0), 2)


	#if any circles
    #if detected_circles is not None:
        #detected_circles = np.uint16(np.around(detected_circles))

		#for all cirlces
        #for pt in detected_circles[0, :]:

          #  a, b, r = pt[0], pt[1], pt[2]  #circle coordinates
          #  cv2.circle(frame, (a, b), r+10, (0, 255, 255), 2)  #draw area around with radius r
         #   cv2.circle(frame, (a, b), 1, (100, 0, 100), 3)  #draw dot im middle


    #cv2.imshow('circles',frame)
    cv2.imshow('cross',cv2.resize(flem, (960, 540)))
    #cv2.imshow('border',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    continue

cap.release()
cv2.destroyAllWindows()