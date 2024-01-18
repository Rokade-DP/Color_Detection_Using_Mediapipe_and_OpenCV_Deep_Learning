# OBJECT DETECTION USING OPENCV

# I Have 3 object with me 1->Red 2-> Green 3->blue

import cv2 # Package of AI

import numpy as np 

# Lets Capture the camera . 0 for webcam. if you want other webcam then we can change to index to 1, 2
cap = cv2.VideoCapture(0)

# Lets Load the Frame
while True:
    _,frame=cap.read()
    
    # we convert this format ho hsv, bgr library this is color format red, green , blue , we are frame with hsv which use to select the color
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    # Lets Frame on the Windowa
    cv2.imshow("Frame", frame)
    
    # weight key event which is 1 and which is 27 then break the loop that means we are going to stop the loop
    key = cv2.waitKey(1)
    if key == 27 :
        break
    
    
# Lets run this one and we will see the camera, camera is on 

# Now lets deeper understanding how to detect color now 

''' HSV --> HUE - we can see the color red,green,blue,yellow and also we can see the gradiation of the color         
          SATURATION - How much quantity of the color we want to have 
          (0- nothing, completely white, opencv - maximux pixel 0-255)
          VALUE - Brightness of the color (0- completely black)'''
#===========          
#Next step is to convert the color format to hsv 