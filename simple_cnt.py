# simple counter 
# for lab.
# use 2 buttons and serial output

from machine import Pin
import time

upsw = Pin(1, Pin.IN, Pin.PULL_UP)
dnsw = Pin(0, Pin.IN, Pin.PULL_UP)

countvalue=0

while True:
    upstate1= upsw.value() 
    time.sleep_us(50)
    upstate2= upsw.value()
    if upstate1 == upstate2:
        if upstate == 0:  #push up button
            countvalue += 1
        else:    #push down button
            countvalue -= 1
        print(countvalue)
        sleep(1)
