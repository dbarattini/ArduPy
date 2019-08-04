from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

led = arduino.addLed(13)    # using led connected to pin 13

led.turnOn()                # turn the led on
time.sleep(1)
led.turnOff()               # turn the led off

led_state = led.getState()  # get led state (1 = on, 0 = off)

arduino.closeConnection()   # close connection to arduino
