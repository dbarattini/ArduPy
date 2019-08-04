from ardupy import *

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

ts = arduino.addTemperatureSensor(A0, lambda voltage : (voltage - .5) * 100)    # using a temperature sensor connected to pin A0
                                                                                # explicited a function for voltage to temperature conversion

temperature = ts.getTemperature()   # returns the temperature calculated

arduino.closeConnection()   # close connection to arduino
