import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://192.168.178.21:5555")

while True:
    fan_speed = 100
    
    print(socket.recv())
    socket.send(fan_speed)
  
    time.sleep(1)