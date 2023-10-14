import cv2
from imutils.video import VideoStream
import time
import os

#cap = cv2.VideoCapture(0,cv2.CAP_V4L2)

#time.sleep(2)
#counter = 0
#while True:
#    ret, frame =cap.read()
#    time.sleep(1)
#    cv2.imshow('test',frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#cap.release()
#cv2.destroyAllWindows()
#cap = VideoStream(usePicamera=True)
#stream = cap.start()
#time.sleep(2)
#counter = 0
#while True:
#    time.sleep(1)
    #frame = stream.read() 
    #cv2.imshow('on PI', frame) 
    #cv2.waitKey(1)
    #os.mkdir('no_smoke')
    #cv2.imwrite(f'./full_smoke/img_{counter}',frame) #no_smoke


from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()
counter = 0
smokelevel = 'middel' # no, full, middel
while True:
    im = picam2.capture_array()
    im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    cv2.imshow('Camera',im)
    cv2.waitKey(1)
    time.sleep(1)
    print(f'./{smokelevel}_smoke/img_{counter}_{smokelevel}_{time.time()}s.jpeg')
    cv2.imwrite(f'./{smokelevel}_smoke/img_{counter}_{smokelevel}_{time.time()}.jpeg',im) 
    counter = counter + 1
