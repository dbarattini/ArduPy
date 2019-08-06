from ardupy import *

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

# using a tilt switch connected to pin 2 (digital)
ts = arduino.addTiltSwitch(2)

while(ts.isOn()):       # returns 1 = yes, 0 = no
    pass

arduino.closeConnection()        # close connection to arduino
