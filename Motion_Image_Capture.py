import cv2
import numpy as np
import time

time.sleep(60) # Delay of 60 seconds 

fp = 'Images/' # Choose the location to store the images
thresh  = 30 # Change threshold for senstitivity
count = 0

cap = cv2.VideoCapture(0) # Acquire Video from the first camera device
ret, frame = cap.read()
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((5,5), np.uint8)

while(ret):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)
    dst = cv2.erode(fgmask,kernel, iterations = 1)
    cv2.imshow('Video', dst) # Comment this line if you do not want to see the video
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to quit the program
        break
    
    ret, frame = cap.read()
    
    if np.mean(dst) > thresh : 
        fn = fp + 'Capture_'+ str(count) + '.png'
        cv2.imwrite(fn, frame)
        count = count + 1
        time.sleep(2)

cap.release()
cv2.destroyAllWindows()
