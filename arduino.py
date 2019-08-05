from ardupy import *

arduino = Arduino("COM5", debug_mode=YES)

arduino.setPin(2, OUTPUT)       # set pin 2 as OUTPUT
arduino.setPin(4, INPUT)        # set pin 4 as INPUT

value = arduino.digitalRead(4)  # read from pin 4   (return 0 | 1)
arduino.digitalWrite(2, HIGH)   # set pin 2 to HIGH ( == 1)
arduino.digitalWrite(2, LOW)    # set pin 2 to LOW  ( == 0)

value = arduino.analogRead(A0)  # read from pin A0  (return value in [0, 1023])

arduino.setPin(3, OUTPUT)       # set pin 3 (pwa) as OUTPUT
arduino.analogWrite(3, 100)     # set pin 3 to 100

arduino.closeConnection()