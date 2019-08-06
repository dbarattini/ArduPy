from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

# using a dc motor connected through a mosfet to pin 9 (pwm)
dc_motor = arduino.addDCMotor(9)

dc_motor.turnOn()                   # turn the motor on (set speed to 255)
time.sleep(5)
dc_motor.turnOff()                  # turn the motor off ( set speed to 0)

time.sleep(5)
# set motor speed to 150 (value in [0, 255])
dc_motor.setSpeed(150)
time.sleep(5)
dc_motor.turnOff()

dc_motor_speed = dc_motor.getSpeed()  # get motor speed (value in [0, 255])

arduino.closeConnection()   # close connection to arduino
