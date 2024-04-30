from goto import *
import time
import var
import pio
import resource
import spidev
import os
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define GPIO to LCD
LCD_RS = 7
LCD_E  = 11
LCD_D4 = 12
LCD_D5 = 13
LCD_D6 = 15
LCD_D7 = 16

# Define GPIO to keypad
R1 = 29
R2 = 31
R3 = 32
R4 = 33
C1 = 36
C2 = 35
C3 = 38
C4 = 37

# Define Sensors
Rain_sensor = 18
flame_Sensor = 40
temp_level  = 22


# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
inputstring = ""
hidekey=""
secretkey = "9922"
delay = 1


