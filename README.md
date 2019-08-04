# Ardupy

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org/)
[![Module](https://img.shields.io/badge/module-pyserial-brightgreen.svg?style=flat)](https://pythonhosted.org/pyserial/)

## About

Framework that allows you to easily control an Arduino Uno with a Raspberry Pi

## Where to start

### Requirements

- python 3.7.3
- pyserial 3.4

install requirements:

```bash
cd Ardupy
pip install -r requirements.txt
```

if you have all the requirements installed, you can start using Ardupy.

## How to use

Upload the [ardupy/ardupy.ino](https://github.com/dbarattini/Ardupy/blob/master/ardupy/ardupy.ino) sketch to your Arduino Uno

Create a new python project and import ardupy

Learn from these examples how to use ardupy:

- [use a button](https://github.com/dbarattini/Ardupy/blob/master/examples/button.py)
- [use a led](https://github.com/dbarattini/Ardupy/blob/master/examples/led.py)
- [use a temperature sensor](https://github.com/dbarattini/Ardupy/blob/master/examples/temperature_sensor.py)
- [use a photoresistor](https://github.com/dbarattini/Ardupy/blob/master/examples/photoresistor.py)
- [use an RGB led](https://github.com/dbarattini/Ardupy/blob/master/examples/led_rgb.py)

## Supported components (for now)

- button
- led
- temperature sensor
- photoresistor
- RGB led
