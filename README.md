# ArduPy

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org/)
[![Module](https://img.shields.io/badge/module-pyserial-brightgreen.svg?style=flat)](https://pythonhosted.org/pyserial/)

## About

ArduPy allows you to easily control transducers connected to an Arduino Uno using Python (ex. using a PC, Raspberry Pi, ...)

## Where to start

### Requirements

- python 3.7.3
- pyserial 3.4

install requirements:

```bash
cd Ardupy
pip install -r requirements.txt
```

if you have all the requirements installed, you can start using ArduPy.

## How to use

Upload the [ardupy/ardupy.ino](https://github.com/dbarattini/Ardupy/blob/master/ardupy/ardupy.ino) sketch to your Arduino Uno

Create a new python project and import ardupy

Learn from these examples:

- [use a button](https://github.com/dbarattini/Ardupy/blob/master/examples/button.py)
- [use a led](https://github.com/dbarattini/Ardupy/blob/master/examples/led.py)
- [use a temperature sensor](https://github.com/dbarattini/Ardupy/blob/master/examples/temperature_sensor.py)
- [use a photoresistor](https://github.com/dbarattini/Ardupy/blob/master/examples/photoresistor.py)
- [use an RGB led](https://github.com/dbarattini/Ardupy/blob/master/examples/led_rgb.py)
- [use a servo](https://github.com/dbarattini/ArduPy/blob/master/examples/servo.py)
- [use a potentiometer](https://github.com/dbarattini/ArduPy/blob/master/examples/potentiometer.py)
- [use a piezo](https://github.com/dbarattini/ArduPy/blob/master/examples/piezo.py)
- [use a tilt switch]()

You can also use ArduPy to comunicate directly to arduino

- [use arduino directly](https://github.com/dbarattini/ArduPy/blob/master/examples/ardupy.py)

## Supported transducers (for now)

- button
- led
- temperature sensor
- photoresistor
- RGB led
- servo
- potentiometer
- piezo
- tilt switch
