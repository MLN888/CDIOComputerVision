import cv2 
import numpy as np 
  
# Read image. 
#img = cv2.imread('eyes3.jpg', cv2.IMREAD_COLOR)
#Test#2
#Test 4

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080) 

while(True):
    ret, frame = cap.read()

    # Convert to grayscale. 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
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
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
    
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
    cv2.imshow("Detected Circle", frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    continue
    #cv2.imwrite("test.png", cap) 
    #cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()