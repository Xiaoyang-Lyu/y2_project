import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   
from gate_indicator import GateIndicator



class DoorIndicator(GateIndicator):
    def __init__(self):
        self.pin = 11
        self.frequency = 50
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
    
    def on_gate_open(self):
        self.pwm.start(5)
        sleep(0.07)
        self.pwm.stop()

    def on_gate_close(self):
        self.pwm.start(9)
        sleep(0.07)
        self.pwm.stop()

    def cleanup(self):
        GPIO.cleanup()

