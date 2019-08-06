from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

# using an h bridge with:
#   enable 1 connected to pin 9
#   input  1 connected to pin 3
#   input  2 connected to pin 2
motor = arduino.addHBridgedDCMotor(9, 3, 2)

motor.turnOn()                  # turn the motor on (set speed to 255)

time.sleep(5)

# set the motor speed to 200 (value in [0, 255])
motor.setSpeed(200)

time.sleep(5)

motor.changeDirection()         # invert the motor direction

time.sleep(5)

motor.turnOff()                 # turn the motor off ( set speed to 0)

value = motor.getSpeed()        # get the motor speed (value in [0, 255])
# get the motor direction (0 -> initial, 1 -> reverse)
value = motor.getDirection()


arduino.closeConnection()
