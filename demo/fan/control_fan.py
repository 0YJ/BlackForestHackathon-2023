# Bibliotheken laden
from machine import Pin, PWM
from time import sleep

# Initialisierung Onboard-LED/PWM-Ausgang
fan1 = PWM(Pin(14, Pin.OUT))

# PWM-Einstellung: Frequenz in Hertz (Hz)
fan1.freq(1000)

i = 0

# Wiederholung (Endlos-Schleife)
while True:
    led.duty_u16(i)
    sleep(0.1)
    i = i + 3000
    if i > 65535:
        i = 0