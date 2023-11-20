# 4-bit up and down counter by using the 2 switches and 4 LEDs
#
# @author = senu
# 20231114
# K4 switch: up
# K3 switch: down

from machine import Pin
import time

#HW cofiguration
#set the 4 LEDs
led0=Pin(0, Pin.OUT)
led1=Pin(1, Pin.OUT)
led2=Pin(2, Pin.OUT)
led3=Pin(3, Pin.OUT)
#2 switches
upsw = Pin(6, Pin.IN,Pin.PULL_UP)
dnsw = Pin(7, Pin.IN,Pin.PULL_UP)

display4bit=[led3,led2,led1,led0]

#function for 4bit display
def display(value):
    # masking 4bits
    value &= 0x0F
    for j in range(4):
        if (value>>j) % 2 == 1:
            display4bit[j].on()
        else:
            display4bit[j].off()

#infinite loop
cntval = 0
onceflag = True

while True:
    #avoid the bounding problem
    upsw_val1 = upsw.value()
    dnsw_val1 = dnsw.value()
    time.sleep_ms(20)
    upsw_val2 = upsw.value()
    dnsw_val2 = dnsw.value()
    
    #check if it is pushed
    if upsw_val1 == upsw_val2:
        if onceflag  and upsw_val2 == 0:
            onceflag = False
            cntval += 1
            if cntval > 15:
                cntval = 0
        elif upsw_val2 == 1:
            onceflag = True
            
    
    if dnsw_val1 == dnsw_val2:
        if onceflag and dnsw_val2 == 0:
            onceflag = False
            cntval -= 1
            if cntval < 0:
                cntval = 15
        elif dnsw_val2 == 1:
            onceflag = True
            
    #display the current value
    display(cntval)
    time.sleep(0.1)

