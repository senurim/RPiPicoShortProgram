# 1st program to display a 4xFND
#
# try to control each segment on the target dig

from machine import Pin
import time

#define output pins and FND elements
dig1 = Pin(13, Pin.OUT, value=1)  #initially turn off
dig2 = Pin(12, Pin.OUT, value=1)
dig3 = Pin(11, Pin.OUT, value=1)
dig4 = Pin(10, Pin.OUT, value=1)


segA = Pin(9, Pin.OUT)