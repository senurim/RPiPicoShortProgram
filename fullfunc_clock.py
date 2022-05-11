#스위치 입력 기능을 가지는 디지털시계 구현하기
#
# 1차 목표: Down 스위치 누르면 날짜/시간 번갈아서 디스플레이함
# 2차 목표: 초 표시까지
# 3차 목표: 스위치 조작을 통한 시간 설정 기능

import fndControl as fnd
from machine import Timer
from machine import RTC
from machine import Pin

#hardware configuration
upsw = Pin(0, Pin.IN, Pin.PULL_UP)
dnsw = Pin(1, Pin.IN, Pin.PULL_UP)

#init RTC
rtc = RTC()

#global variables
currentDigit = 0  #current digit counter 0~3
displayNumber=[0,0,0,0 ]  #default values of 4 numbers
dotFlag=[False,True,False,False]  #DP segment ON/OFF info for each digit
disMode=0  #display mode variable 0:display time, 1: date MM.DD, 2: seconds __SS
setMode=False   #time setting flag variable , if True, then time setting mdoe


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
    global disMode

    if disMode == 0 : # mode 0; displya HH:MM
        cTime = rtc.datetime()
        displayNumber=[cTime[4]//10, cTime[4]%10, cTime[5]//10, cTime[5]%10]
        dotFlag[3] = False
        dotFlag[1] = not dotFlag[1]

    elif disMode == 1: #mode 1: mm:dd
        cTime = rtc.datetime()
        displayNumber=[cTime[1]//10, cTime[1]%10, cTime[2]//10, cTime[2]%10]
        dotFlag[1] = dotFlag[3] = True
    
    elif disMode == 2: #mode 2: __:ss
        cTime = rtc.datetime()
        displayNumber=[16,16, cTime[6]//10, cTime[6]%10]
        dotFlag[1] = not dotFlag[1]
        dotFlag[3] = not dotFlag[3]

        

def upSWcb(upsw):
    '''
    upSWcb() function: up switch callback function
    This functions called when the user pushes the UP switch. Then change the display mode (increase value)
    '''
    global disMode
    disMode += 1
    disMode %= 3    #first try

def downSWcb(dnsw):
    global disMode
    

# initialize the IRQs of Pins
upsw.irq(upSWcb, trigger=Pin.IRQ_FALLING )
dnsw.irq(downSWcb, trigger=Pin.IRQ_FALLING )


#run timers
dd_tmr=Timer(period=5, mode=Timer.PERIODIC, callback=dd_cb)
halfsectmr=Timer(period=500, mode=Timer.PERIODIC, callback=halfsec_cb)  
