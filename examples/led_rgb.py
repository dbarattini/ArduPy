from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

led_rgb = arduino.addLedRGB(6, 5, 3)    # using an rgb led connected like:
#   RED   -> pin 6
#   GREEN -> pin 5
#   BLUE  -> pin 3

led_rgb.setRedValue(150)    # sets red color to 150 (value in [0, 255])
led_rgb.setGreenValue(100)
led_rgb.setBlueValue(50)

# returns a dictionary line {"red": 150, "green": 100, "blue": 50}
values = led_rgb.getValues()

led_rgb.setRedValue(0)
led_rgb.setGreenValue(0)
led_rgb.setBlueValue(0)

arduino.closeConnection()   # close connection to arduino
