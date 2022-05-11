# FND 제어를 위한 여러 함수를 모듈 방식으로 재편성함.
# module name: fndControl.py
#
from machine import Pin
import time

#define output pins and FND elements
dig1 = Pin(13, Pin.OUT, value=1)  #initially turn off
dig2 = Pin(12, Pin.OUT, value=1)
dig3 = Pin(11, Pin.OUT, value=1)
dig4 = Pin(10, Pin.OUT, value=1)

digitLst = [dig1, dig2, dig3, dig4]

segA=Pin(9,Pin.OUT)
segB=Pin(8,Pin.OUT)
segC=Pin(7,Pin.OUT)
segD=Pin(6,Pin.OUT)
segE=Pin(18,Pin.OUT)
segF=Pin(19,Pin.OUT)
segG=Pin(20,Pin.OUT)
segDP=Pin(21,Pin.OUT)

segLst=[segA, segB, segC, segD, segE, segF, segG]

# 0~9 mapping table
segmap = [ [1,1,1,1,1,1,0], [0,1,1,0,0,0,0], [1,1,0,1,1,0,1], [1,1,1,1,0,0,1], [0,1,1,0,0,1,1], [1,0,1,1,0,1,1],\
          [1,0,1,1,1,1,1], [1,1,1,0,0,0,0], [1,1,1,1,1,1,1], [1,1,1,1,0,1,1], [1,1,1,0,1,1,1], [0,0,1,1,1,1,1],\
          [1,0,0,1,1,1,0], [0,1,1,1,1,0,1], [1,0,0,1,1,1,1], [1,0,0,0,1,1,1], [0,0,0,0,0,0,0] ]

#global variables
#display on flag
displayOnState = False
#time duration for dynamic driving
displayRate = 5000  #unit micro sec, default = 5 msec


#define a function to display one number on 7segments unit
def displayNumber(num):
    '''
    Display one number at one 7 segment
    parameter: num - 0 ~ 15 integer number to be displayed, and ' '(space character) for blank(empty)
    '''
    if num >= 0 and num <= 16: #check the valid range
        mapinfo = segmap[num]
        for i in range(7):
            segLst[i].value(mapinfo[i])
    else:
        print('Err:out of range in displayed number')
        return -1

def displayDigitOne(digit, num, dpOn=False):
    '''
    a function to display one number at the given digit
    -parameter: digit - 0 ~ 3 (left to right), num - 0 ~ 15, dpOn: DP on/off default=False 
    '''
    if digit >= 0 and digit <=3 :
        digitLst[digit].value(0)      #turn on the given digit
    else:
        print('Err: out of range for digit')
        return -1

    displayNumber(num)

    if dpOn:
        segDP.on()
    else:
        segDP.off()

def turnoffDigit(digit):
    '''
    Turn off the given digit segment
    -parameter: digit - 0 ~ 3 (left to right)
    '''
    digitLst[digit].value(1)

def turnoff4Fnd():
    '''
    Turn off the 4 digits 7 segments
    '''
    global displayOnState
    if displayOnState:
        displayOnState = False
        for i in range(4):
            turnoffDigit(i)
    
def onoffDP(digit, flag):
    '''
    Turn on the given digit's DP (dot)
    '''
    if digit >= 0 and digit <=3 :
        if flag:
            digitLst[digit].value(0)      #turn on the given digit
            segDP.value(1)
        else:
             digitLst[digit].value(1)      #turn off the given digit
             segDP.value(0)
    else:
        print('Err: wrong digit')
        return 
    