import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
import time 
GPIO.setwarnings(False)
from gate_indicator import GateIndicator

class DoorIndicator(GateIndicator):
    def __init__(self):       
        GPIO.setmode(GPIO.BCM)
        servo_pin = 17
        GPIO.setup(servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(servo_pin, 50)
        self.pwm.start(0)

    def on_gate_open(self):
        #set angle 90
        angle=90
        duty_cycle = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)
        self.pwm.ChangeDutyCycle(0)

    def on_gate_close(self):
        #set angle 0
        angle=0
        duty_cycle = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)
        self.pwm.ChangeDutyCycle(0)



'''
#test
m = DoorIndicator()

while True:
    m.on_gate_open()
    time.sleep(1)
    m.on_gate_close()
    time.sleep(1)
'''
