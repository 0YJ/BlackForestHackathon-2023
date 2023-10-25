import imagezmq
import socket
import cv2
from imutils.video import VideoStream

cap = VideoStream()

sender = imagezmq.ImageSender() 

cam_id = socket.gethostname()
stream = cap.start()

while True:
    frame = stream.read() 
    sender.send_image(cam_id, frame)

python 
