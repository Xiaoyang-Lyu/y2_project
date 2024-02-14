import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   

class DoorController:
    def __init__(self, pin, frequency):
        self.pin = 11
        self.frequency = 50
        GPIO.setmode(GPIO.BOARD)  # Sets the pin numbering system to use the physical layout
        GPIO.setup(self.pin, GPIO.OUT)  # Sets up pin to an output
        self.pwm = GPIO.PWM(self.pin, self.frequency)  # Sets up pin as a PWM pin

    def door_open(self):  # turn 90 degree
        self.pwm.start(5)
        sleep(0.07)
        self.pwm.stop()

    def door_close(self):  # turn -90 degree
        self.pwm.start(9)
        sleep(0.07)
        self.pwm.stop()

    def cleanup(self):
        GPIO.cleanup()  # Cleans up the GPIO pins

#test
#door_open()
#door_close()

 
#GPIO.cleanup() 
