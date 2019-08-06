import serial
import time

OUTPUT = 1
INPUT = 0
HIGH = 1
LOW = 0
OFF = 0
ON = 1
A0 = 14
A1 = 15
A2 = 16
A3 = 17
A4 = 18
A5 = 19
A6 = 20
A7 = 21
YES = 1
NO = 0


class Arduino:
    def __init__(self, port="COM1", baudrate=9600, debug_mode=NO):
        self.conn = serial.Serial(port, baudrate)
        print("ARDUINO: CONNECTED")
        self.conn.readline()
        self.conn.readline()
        self.conn.readline()
        self.debug_mode = debug_mode

    def setPin(self, pin, _type):
        self.conn.write(("<pinMode, " + str(pin) +
                         ", " + str(_type) + ">").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()

    def digitalWrite(self, pin, value):  # value = 0 | 1
        self.conn.write(("<digitalWrite, " + str(pin) +
                         ", " + str(value) + ">").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()

    def digitalRead(self, pin):         # value = 0 | 1
        self.conn.write(("<digitalRead, " + str(pin) + ", 0>").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()
        return int(self.conn.readline().decode())

    def analogWrite(self, pin, value):  # value in [ 0 , 255 ]
        self.conn.write(("<analogWrite, " + str(pin) +
                         ", " + str(value) + ">").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()

    def analogRead(self, pin):          # value in [ 0 , 1023 ]
        self.conn.write(("<analogRead, " + str(pin) + ", 0>").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()
        return int(self.conn.readline().decode())

    def servoAttach(self, pin):
        self.conn.write(("<servoAttach, " + str(pin) + " , 0>").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()
        return int(self.conn.readline().decode())

    def servoWrite(self, name, value):
        self.conn.write(("<servoWrite, " + str(name) +
                         ", " + str(value) + ">").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()

    def tone(self, pin, pitch, time):
        self.conn.write(
            ("<tone, " + str(pin) + ", " + str(pitch) + ">").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()
        self.conn.write(
            ("<tone, " + str(pin) + ", " + str(time) + ">").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()

    def noTone(self, pin):
        self.conn.write(
            ("<noTone, " + str(pin) + ", 0>").encode())
        self.conn.flush()
        if(self.debug_mode):
            print("ARDUINO:", self.conn.readline().decode(), end="")
        else:
            self.conn.readline().decode()

    def addLed(self, pin):
        return Led(pin, self)

    def addButton(self, pin):
        return Button(pin, self)

    def addTemperatureSensor(self, pin, voltageToTemp=lambda voltage:  (voltage - .5) * 100):
        return TemperatureSensor(pin, self, voltageToTemp)

    def addPhotoresistor(self, pin):
        return Photoresistor(pin, self)

    def addLedRGB(self, pin_r, pin_g, pin_b):
        return LedRGB(pin_r, pin_g, pin_b, self)

    def addServo(self, pin):
        return Servo(pin, self)

    def addPotentiometer(self, pin):
        return Potentiometer(pin, self)

    def addPiezo(self, pin):
        return Piezo(pin, self)

    def addTiltSwitch(self, pin):
        return TiltSwitch(pin, self)

    def addDCMotor(self, pin):
        return DCMotor(pin, self)

    def closeConnection(self):
        self.conn.close()


class Led:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host
        self.state = OFF
        host.setPin(pin, OUTPUT)

    def turnOn(self):
        self.host.digitalWrite(self.pin, ON)
        self.state = ON

    def turnOff(self):
        self.host.digitalWrite(self.pin, OFF)
        self.state = OFF

    def getState(self):
        return self.state


class Button:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host
        host.setPin(pin, INPUT)

    def isPressed(self):
        return self.host.digitalRead(self.pin)


class TemperatureSensor:
    def __init__(self, pin, host, voltageToTemp):
        self.pin = pin
        self.host = host
        self.voltageToTemp = voltageToTemp

    def getTemperature(self):
        sensorVal = self.host.analogRead(self.pin)
        voltage = (sensorVal/1024.0) * 5.0
        return self.voltageToTemp(voltage)


class Photoresistor:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host

    def getValue(self):
        return self.host.analogRead(self.pin)


class LedRGB:
    def __init__(self, pin_r, pin_g, pin_b, host):
        self.pin_r = pin_r
        self.pin_g = pin_g
        self.pin_b = pin_b
        self.host = host
        self.values = {"red": 0, "green": 0, "blue": 0}
        host.setPin(pin_r, OUTPUT)
        host.setPin(pin_g, OUTPUT)
        host.setPin(pin_b, OUTPUT)

    def setRedValue(self, value):
        self.host.analogWrite(self.pin_r, value)
        self.values["red"] = value

    def setGreenValue(self, value):
        self.host.analogWrite(self.pin_g, value)
        self.values["green"] = value

    def setBlueValue(self, value):
        self.host.analogWrite(self.pin_b, value)
        self.blue_value = value
        self.values["blue"] = value

    def getValues(self):
        return self.values


class Servo:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host
        self.degrees = 0
        self.name = host.servoAttach(pin)
        if(self.name == -1):
            raise IndexError(
                'Too many Servos! If you want to add more Servos you have to modify the maxServos constant in ardupy.ino')

    def rotate(self, degrees):
        self.host.servoWrite(self.name, degrees)
        self.degrees = degrees

    def getPosition(self):
        return self.degrees


class Potentiometer:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host

    def getValue(self):
        return self.host.analogRead(self.pin)


class Piezo:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host

    def tone(self, pitch, time):  # time in milliseconds
        self.host.tone(self.pin, pitch, time)

    def noTone(self):
        self.host.noTone(self.pin)


class TiltSwitch:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host
        host.setPin(pin, INPUT)

    def isOn(self):
        return self.host.digitalRead(self.pin)


class DCMotor:
    def __init__(self, pin, host):
        self.pin = pin
        self.host = host
        self.speed = 0
        host.setPin(pin, OUTPUT)

    def turnOn(self):
        self.host.digitalWrite(self.pin, ON)
        self.speed = 255

    def turnOff(self):
        self.host.digitalWrite(self.pin, OFF)
        self.speed = 0

    def setSpeed(self, speed):
        self.host.analogWrite(self.pin, speed)
        self.speed = speed

    def getSpeed(self):
        return self.speed
