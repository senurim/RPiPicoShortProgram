# 타이머 IRQ 기반 4FND 다이나믹 구동 방법 구현한 소스에 RTC 정보 사용하여 시계 구현하기
#


import fndControl as fnd
from machine import Timer
from machine import RTC


#init RTC
rtc = RTC()

#global variables
currentDigit = 0  #current digit counter 0~3
displayNumber=[0,0,0,0 ]  #default values of 4 numbers
dotFlag=[False,True,False,False]  #DP segment ON/OFF info for each digit

#use two different timers
# first: 0.5sec timer -- toggling 2nd digit DP seg.
# second: 5msec timer -- change the displayed digit with the given data

def dd_cb(dd_tmr): 
    '''
    Callback function for dynamic driving
     - major role: change to the digit turned on
    '''
    global currentDigit

    #at first turn the current digit OFF
    fnd.turnoffDigit(currentDigit)

    #change the digit
    currentDigit += 1
    currentDigit %= 4
    fnd.displayDigitOne(currentDigit, displayNumber[currentDigit], dotFlag[currentDigit])

    
def halfsec_cb(halfsectmr):
    #callback function for half second period (0.5sec)
    #major role: 현재 시각 정보 갖고 오기 & dp pin toggling
    global dotFlag
    global displayNumber

    dotFlag[1] = not dotFlag[1]

    cTime = rtc.datetime()
    displayNumber=[cTime[4]//10, cTime[4]%10, cTime[5]//10, cTime[5]%10]

        

#run timers
dd_tmr=Timer(period=5, mode=Timer.PERIODIC, callback=dd_cb)
halfsectmr=Timer(period=500, mode=Timer.PERIODIC, callback=halfsec_cb)  
