import cv2
import base64
import zmq
import numpy as np
import argparse
import logging
from ultralytics import YOLO

# zmq socket set for communication with the pi
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://192.168.175.0:6666")

# set up logging
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)

# add argparse to configure YOLOv8 and other parameters if necessary
parser = argparse.ArgumentParser(description="Smoke detection and fan control")
parser.add_argument("--weights", type=str, default="yolov8.weights", help="path to the weights file")
parser.add_argument("--cfg", type=str, default="yolov8.cfg", help="path to the cfg file")
parser.add_argument("--names", type=str, default="yolov8.names", help="path to the names file")
args = parser.parse_args()

# load yolo model
model = YOLO('best.pt')
#model.train(data='xxxx', epoh=100)

# validation 
metrics = model.val()
metrics.top1
metrics.top5

results = model.predict("xx")
probs = result.probs
print(probs.data)

tensor([xxx])
# control the fan based on smoke density
def control_fan(smoke_density):
    if smoke_density == 0:
        # no smoke detected, stop the fan
        logging.info("No smoke detected, fan stopped.")
    elif smoke_density == 1:
        # middle smoke detected, fan running at low speed
        logging.info("Light smoke detected, fan running at low speed.")
    elif smoke_density == 2:
        # full smoke detected, fan running at full speed
        logging.info("Heavy smoke detected, fan running at full speed")

try:
    while True:
        # receive the Base64 encoded frame from the Raspberry Pi
        frame_as_base64 = socket.recv()
        
        # decode the frame from Base64
        buffer = base64.b64decode(frame_as_base64)
        frame = cv2.imdecode(np.frombuffer(buffer, np.uint8), -1)

        # continue with smoke density calculation as in your original code

        # detect objects, specifically "smoke," in the frame using YOLOv8
        results = yolo.detect(frame)

        # extract the smoke region and calculate its density
        smoke_region = np.zeros_like(frame, dtype=np.uint8)
        for detection in results:
            if detection["name"] == "smoke" and detection["confidence"] > 0.5:
                x, y, w, h = detection["box"]
                # extract the smoke region
                smoke_region[y:y+h, x:x+w] = frame[y:y+h, x:x+w]

        # convert the image to grayscale
        gray = cv2.cvtColor(smoke_region, cv2.COLOR_BGR2GRAY)

        # threshold the image to separate smoke from the background
        _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # calculate the number of white pixels (smoke pixels)
        white_pixels = cv2.countNonZero(binary)

        # calculate density
        density = white_pixels / (smoke_region.shape[0] * smoke_region.shape[1])

        # define whatz are smoke density levels
            smoke_density = 0  # default to no smoke
        if density < 0.1:
            smoke_density = 0  # no smoke
        elif density < 0.5:
            smoke_density = 1  # middle smoke
        else:
            smoke_density = 2  # full smoke

        # control the fan
        control_fan(smoke_density)

        # display the frame with smoke density and fan status information
        text_color = (0, 255, 0)  # Green
        if smoke_density == 1:
            text_color = (0, 255, 255)  # Yellow
        elif smoke_density == 2:
            text_color = (0, 0, 255)  # Red
        cv2.putText(frame, f"Smoke density: {smoke_density}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        cv2.imshow("Smoke Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

# close the socket
socket.close()

