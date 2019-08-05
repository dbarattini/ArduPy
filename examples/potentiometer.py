from ardupy import *

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

# using a potentiometer connected to pin A0
pot = arduino.addPotentiometer(A0)

# returns the value of the potentiometer in [0, 1023]
value = pot.getValue()

arduino.closeConnection()   # close connection to arduino
