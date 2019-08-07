from ardupy import *
import time

# ardupy.ino use LiquidCrystal.h

# arduino connected to port COM5 with baudrate 9600
arduino = Arduino("COM5", debug_mode=YES)

# ! in ardupy.ino you have to modify this lines before you upload the sketch to arduino:
#
#   // if you are using an LCD comment the first line and uncomment and modify the second line
#   //LiquidCrystal lcd(-1, -1, -1, -1, -1, -1) //! FAKE lcd (can't initialize without constructor)
#   LiquidCrystal lcd(12, 11, 5, 4, 3, 2)       //! REAL lcd (modify with your pins)
#   // when you are not using an lcd uncomment the first line and comment the second

lcd = arduino.addLCD()        # using an lcd defined in ardupy.ino
lcd.begin(16, 2)              # lcd's columns = 16 , rows = 2

lcd.print("Hello World!")     # print on the display "Hello World!"

time.sleep(5)

lcd.clear()                   # clear the display
lcd.print("LCD Test")

time.sleep(5)
lcd.clear()

arduino.closeConnection()
