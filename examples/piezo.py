from ardupy import *
import time

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

piezo_out = arduino.addPiezo(8)    # using a piezo connected to pin 8 (digital) as output

# calls arduino tone function with pitch = 50 and duration = 100ms
piezo_out.tone(50, 100)

piezo_out.noTone()                 # calls arduino noTone function that stops the piezo

piezo_out.tone(50, 100)

piezo_in = arduino.addPiezo(A0)     # using a piezo connected to pin A0 (analog) as input

value = piezo_in.getValue()         # returns the perceived value


arduino.closeConnection()      # close connection to arduino
