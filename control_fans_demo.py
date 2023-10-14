import zmq
import time
import RPi.GPIO as GPIO


FAN1 = 18
FAN2 = 23
def setup_gpio():
    GPIO.setmode(GPIO.BCM)   
    GPIO.setup(FAN1, GPIO.OUT)
    GPIO.setup(FAN2, GPIO.OUT)

def shutdown():
     GPIO.cleanup()


def main():
    fan1 = setup_gpio()


    GPIO.output(FAN1,False)
    GPIO.output(FAN2,False)

    while True:
        GPIO.output(FAN1,True)
        GPIO.output(FAN2,False)
        time.sleep(5)
        print('Change Fan')
        GPIO.output(FAN1,False)
        GPIO.output(FAN2,True)
        time.sleep(5)

	
    shutdown()

if __name__ == '__main__':
    main()
