from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

try:
    servo = arduino.addServo(6)  # using a servo connected to pin 9
except  IndexError as e:
    # message: 'Too many Servos! If you want to add more Servos you have to modify the maxServos constant in ardupy.ino'
    print(str(e))
    exit(-1)

servo.rotate(0)            # rotate the servo in position = 0 degree
print(servo.getPosition()) # initial position = 0 degree

time.sleep(1)

servo.rotate(90)            # rotate the servo in position = 45 degree
print(servo.getPosition())  # returns 45

time.sleep(1)

servo.rotate(0)             # return to initial position

arduino.closeConnection()
