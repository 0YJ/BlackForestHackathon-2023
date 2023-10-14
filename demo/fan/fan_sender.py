import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.STREAM)

socket.connect('tcp://localhost:5555')
id_sock = socket.getsockopt(zmq.IDENTITY)
socket.send(id_sock, zmq.SNDMORE)
fan_speed = 100
socket.send(fan_speed)
#while True:
#    fan_speed = 100
#    print('123')
#    socket.send(fan_speed)
#    time.sleep(2)
