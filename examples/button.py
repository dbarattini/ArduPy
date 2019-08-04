from ardupy import *

arduino = Arduino("COM5", debug_mode=YES)   # arduino connected to port COM5 with baudrate 9600

button = arduino.addButton(2)    # using button connected to pin 2

while(button.isPressed()):       # returns 1 = yes, 0 = no
    pass

arduino.closeConnection()        # close connection to arduino
