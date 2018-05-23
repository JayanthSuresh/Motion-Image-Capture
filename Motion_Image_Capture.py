import cv2
import numpy as np
import time

time.sleep(60)

fp = 'Images/'
count = 0

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((5,5), np.uint8)

while(ret):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)
    dst = cv2.erode(fgmask,kernel, iterations = 1)
    #cv2.imshow('Video', dst)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    ret, frame = cap.read()
    
    if np.mean(dst) > 30 :
        fn = fp + 'Capture_'+ str(count) + '.png'
        cv2.imwrite(fn, frame)
        count = count + 1
        time.sleep(2)

cap.release()
cv2.destroyAllWindows()
