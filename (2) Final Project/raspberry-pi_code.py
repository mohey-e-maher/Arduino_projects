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


#define the write & earse to the screen
GPIO.setup(LCD_E, GPIO.OUT)  # E (Earse the screen)
GPIO.setup(LCD_RS, GPIO.OUT) # RS (write to the screen)
# the first 4 binary input
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

#define the keypad buttons
GPIO.setup(R1, GPIO.OUT) # DB7
GPIO.setup(R2, GPIO.OUT) # DB7
GPIO.setup(R3, GPIO.OUT) # DB7
GPIO.setup(R4, GPIO.OUT) # DB7
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#define sensors pins
GPIO.setup(Rain_sensor, GPIO.IN)
GPIO.setup(flame_Sensor, GPIO.IN)
GPIO.setup(temp_level, GPIO.IN)

# Define device screen constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line


