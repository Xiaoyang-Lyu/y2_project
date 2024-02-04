import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout


GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output 
pwm = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin

def door_open():    #turn 90 degree
    pwm.start(5)               
    sleep(0.07)    
    pwm.stop()     
	

def door_close():   #turn -90 degree
    pwm.start(9)               
    sleep(0.07)    
    pwm.stop()  

#test
#door_open()
#door_close()

 
#GPIO.cleanup() 
