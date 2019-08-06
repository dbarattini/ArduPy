from ardupy import *

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

pr = arduino.addPhotoresistor(A0)   # using a photoresistor connected to pin A0 (analog)

value = pr.getValue()               # returns the value of the photoresistor in [0, 1023]

arduino.closeConnection()   # close connection to arduino
