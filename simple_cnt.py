# simple counter 
# for lab.
# use 2 buttons and serial output

from machine import Pin
import time

upsw = Pin(1, Pin.IN, Pin.PULL_UP)
dnsw = Pin(0, Pin.IN, Pin.PULL_UP)

onceflag = True
countvalue=0

while True:
    #double reading for debouncing
    #check up switch
    state1= upsw.value() 
    time.sleep_us(100)
    state2= upsw.value()
    if state1 == state2 : #push a button
        if state1 == 0 and onceflag :  #check already count
            countvalue += 1
            onceflag = False
            print(countvalue)
        elif state1 == 1:    #no push
            onceflag = True
        
    #check down switch
    state1= dnsw.value() 
    time.sleep_us(100)
    state2= dnsw.value()
    if state1 == state2 : #push a button
        if state1 == 0 and onceflag :  #check already count
            countvalue -= 1
            onceflag = False
            print(countvalue)
        elif state1 == 1:    #no push
            onceflag = True
        
    
    time.sleep_ms(100)
