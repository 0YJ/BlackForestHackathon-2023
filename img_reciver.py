import base64
import cv2
import numpy as np
import zmq
import time
# zmq socket set for communication with the pi
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://192.168.178.21:6666")
print('bind')
int = 0
while True:
    image = socket.recv()
    print(type(image))
    #grey = cv2.cvtColor(frame_as_base64, cv2.COLOR_BAYER_BG2GRAY)
    print('recv')  
    cv2.imshow('t',image)
    cv2.waitKey(1)
    print('imwrite')  
   # cv2.imwrite('data_{i}.jpeg',frame,)
    i = i +1