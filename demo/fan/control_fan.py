import zmq
import time
import RPi.GPIO as GPIO

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
 
    p = GPIO.PWM(14, 50)  # frequency=50Hz
    p.start(100)


def set_fan_speed(pwm_pin,speed:int):
    pwm_pin.ChangeDutyCycle(speed)
    time.sleep(0.1)

def shutdown(pwm_pin):
    pwm_pin.stop()
    GPIO.cleanup()

def setup_zmq():
    context = zmq.Context()
    socket = context.socket(zmq.STREAM)

    socket.bind('tcp://*:5555')
    
    return socket

def main():
    socket = setup_zmq()
    setup_gpio()
    
    while True:
        id_sock = socket.recv()
        assert not socket.recv()    # empty data here
        assert socket.recv() == id_sock
        message = socket.recv()
        print('received:', message)
        set_fan_speed(message)
    shutdown()