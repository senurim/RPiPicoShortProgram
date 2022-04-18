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
segmap = {0:[1,1,1,1,1,1,0], 1:[0,1,1,0,0,0,0], 2:[1,1,0,1,1,0,1],\
          3:[1,1,1,1,0,0,1], 4:[0,1,1,0,0,1,1], 5:[1,0,1,1,0,1,1],\
          6:[1,0,1,1,1,1,1], 7:[1,1,1,0,0,0,0], 8:[1,1,1,1,1,1,1],\
          9:[1,1,1,1,0,1,1], 10:[1,1,1,0,1,1,1], 11:[0,0,1,1,1,1,1],\
          12:[1,0,0,1,1,1,0], 13:[0,1,1,1,1,0,1], 14:[1,0,0,1,1,1,1],\
          15:[1,0,0,0,1,1,1]}

#define a function to display one number on 7segments unit
def displayNumber(num):
    '''
    Display one number at one 7 segment
    parameter: num - 0 ~ 15 integer number to be displayed
    '''
    if num >= 0 and num < 16: #check the valid range
        mapinfo = segmap[num]
        for i in range(7):
            segLst[i].value(mapinfo[i])
    else:
        mapinfo = segmap[14]
        for i in range(7):
            segLst[i].value(mapinfo[i])

def displayDigitOne(digit, num):
    '''
    a function to display one number at the given digit
    -parameter: digit - 0 ~ 3 (left to right), num - 0 ~ 15 
    '''
    if digit >= 0 and digit <=3 :
        digitLst[digit].value(0)      #turn on the given digit
    else:
        print('Err: wrong digit')

    displayNumber(num)

def turnoffDigit(digit):
    '''
    Turn off the given digit segment
    -parameter: digit - 1 ~ 4 (left to right)
    '''
    digitLst[digit].value(1)

digitcnt = 0
for i in range(16):
    displayDigitOne(digitcnt,i)
    time.sleep(1)
    turnoffDigit(digitcnt)
    digitcnt += 1
    digitcnt %= 4
