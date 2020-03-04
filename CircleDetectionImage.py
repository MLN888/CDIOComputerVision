import cv2 
import numpy as np 

#https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
# Read image. 
#img = cv2.imread('eyes.jpg', cv2.IMREAD_COLOR) 


cap = cv2.VideoCapture(cv2.CAP_DSHOW + 1)
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap.set(cv2.cv.CV_CAP_PROP_FOURCC, cv2.cv.CV_FOURCC('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720) 
  
# Convert to grayscale. 
ret, img = cap.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (3, 3)) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) 
  
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
        print(a)
        print(b)
        cv2.imshow("Detected Circle", img) 
        cv2.imwrite("test.png", img) 
        cv2.waitKey(0) 
