from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

dc_motor = arduino.addDCMotor(9)    # using a dc motor connected through a mosfet to pin 9 (digital)

dc_motor.turnOn()                   # turn the motor on
time.sleep(1)
dc_motor.turnOff()                  # turn the motor off

dc_motor_state = dc_motor.getState()  # get motor state (1 = on, 0 = off)

arduino.closeConnection()   # close connection to arduino
