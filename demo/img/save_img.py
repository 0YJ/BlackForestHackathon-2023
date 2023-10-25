import cv2
from imutils.video import VideoStream
import time
import os

cap = VideoStream()
stream = cap.start()
time.sleep(2)
counter = 0
while True:
    time.sleep(1)
    frame = stream.read() 
    cv2.imshow('on PI', frame) 
    cv2.waitKey(1)
    os.mkdir('no_smoke')
    #cv2.imwrite(f'./no_smoke/img_{counter}',frame) 
