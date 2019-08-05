from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

piezo = arduino.addPiezo(8)    # using a piezo connected to pin 8

piezo.tone(50, 100)            #  calls arduino tone function with pitch = 50 and duration = 100ms

arduino.closeConnection()      # close connection to arduino