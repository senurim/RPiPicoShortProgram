# simulate the 4-bit counter by using the 4 LEDs on the board
#
# @author = senu
# 20231114
from machine import Pin
import time

#set the 4 LEDs
led0=Pin(0, Pin.OUT)
led1=Pin(1, Pin.OUT)
led2=Pin(2, Pin.OUT)
led3=Pin(3, Pin.OUT)

counter=[led3,led2,led1,led0]

#infinite loop
while True:
    for i in range(16): #couting up from 0 to 15
        #binstr = bin(i)
        for j in range(4):
            if (i>>j) % 2 == 1:
                counter[j].on()
            else:
                counter[j].off()
        time.sleep(0.5)

