import imagezmq
import socket
import cv2
from imutils.video import VideoStream

cap = VideoStream()

# change this to your server address
sender = imagezmq.ImageSender()#(connect_to='tcp://localhost:5555') 

cam_id = socket.gethostname()
stream = cap.start()

while True:
    frame = stream.read() 
    sender.send_image(cam_id, frame)

python 