#스위치 입력 기능을 가지는 디지털시계 구현하기
#
# 1차 목표: Down 스위치 누르면 날짜/시간 번갈아서 디스플레이함
# 2차 목표: 초 표시까지
# 3차 목표: 스위치 조작을 통한 시간 설정 기능
#       3.1 오래 누르기 감지 기능 추가 (setting mode / running mode change)
#            1.5초 이상 누르면 작동
#       3.2 setting mode: time tuple (year, month, day, hour, min) 설정하기

import fndControl as fnd
from machine import Timer
from machine import RTC
from machine import Pin

#hardware configuration
modesw = Pin(0, Pin.IN, Pin.PULL_UP)
setsw = Pin(1, Pin.IN, Pin.PULL_UP)

#init RTC
rtc = RTC()

#global variables
currentDigit = 0  #current digit counter 0~3
displayNumber=[0,0,0,0 ]  #default values of 4 numbers
dotFlag=[False,True,False,False]  #DP segment ON/OFF info for each digit
disMode=0  #display mode variable 0:display time, 1: date MM.DD, 2: seconds __SS
longSwCnt = 0 # long time switch pressing counter that is increased in 0.5sec IRQ handler
setMode = False   #time setting flag variable , if True, then time setting mdoe
cTime=(2022,5,17,2,12,0,0,0)
blinkFlag = True

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
    global setMode
    global longSwCnt
    global cTime
    global blinkFlag

    cTime = rtc.datetime()

    # handling for longSwCnt 
    if longSwCnt != 0:  #press set button once
        #read the set sw value
        if setsw.value() == 0:  #pressed ?
            longSwCnt += 1
        else:
            longSwCnt = 0   #reset the counter

    
    if longSwCnt == 4: #more than 1.5sec then change the mode btwn set/display
        longSwCnt = 0
        if not setMode:
            setMode = True
            disMode = 0
        else:
            setMode = False
            disMode = 0
    
    # handling display for two modes
    # 
    if not setMode: # In normal mode
        if disMode == 0 : # mode 0; displya HH:MM
            displayNumber=[cTime[4]//10, cTime[4]%10, cTime[5]//10, cTime[5]%10]
            dotFlag= [False, not dotFlag[1], False, False]
            
        elif disMode == 1: #mode 1: mm:dd
            displayNumber=[cTime[1]//10, cTime[1]%10, cTime[2]//10, cTime[2]%10]
            dotFlag=[ False, True, False, True]
        
        elif disMode == 2: #mode 2: __:ss
            displayNumber=[16,16, cTime[6]//10, cTime[6]%10]
            dotFlag = [ False, not dotFlag[1], False, not dotFlag[3]]
        
    else: # In setting mode
        if disMode == 0 : # mode 0; displya H.H._ _
            displayNumber=[cTime[4]//10, cTime[4]%10, 16, 16 ]
            dotFlag=[True, True, False, False]
        
        elif disMode == 1 : # mode 1; displya _ _M.M.
            displayNumber=[16, 16, cTime[5]//10, cTime[5]%10 ]
            dotFlag=[False, False, True, True]
        
        elif disMode == 2 : # mode 2; displya mm._ _
            displayNumber=[cTime[1]//10, cTime[1]%10, 16, 16 ]
            dotFlag=[False, True, False, False]
        elif disMode == 3 : # mode 3; displya _ _.dd
            displayNumber=[16, 16, cTime[2]//10, cTime[2]%10 ]
            dotFlag=[False, True, False, False]
        
        
def modeSWcb(modesw):
    '''
    modeSWcb() function: mode switch callback function
    This function handle the mode switch clicking events:
      Normal mode: pushing this switch to change the display mode
      Setting mode: increase the value of each digits
    '''
    global disMode
    global setMode
    global cTime

    if not setMode:
        disMode += 1
        disMode %= 3    
    else: # in setting mode increase the value
        newTS = list(cTime)
        if disMode == 0: #increase HH
            newTS[4] += 1
            if newTS[4] > 23:
                newTS[4] = 0
        elif disMode == 1: #increase MM
            newTS[5] += 1
            if newTS[5] > 59:
                newTS[5] = 0
        elif disMode == 2: #increase mm
            newTS[1] += 1
            if newTS[1] > 12:
                newTS[1] = 1
        elif disMode == 3: #increase mm
            newTS[2] += 1
            if newTS[2] > 31:
                newTS[2] = 1    

        #set up rtc
        rtc.datetime(newTS)



def setDownSWcb(setsw):
    '''
    setDownSwcb() function: setting switch callback function
    The role of thi CB func: start to count the longSwCnt variable
    '''
    # global setMode
    global longSwCnt
    global disMode
    global setMode

    
    longSwCnt = 1
    
    if setMode:
        disMode += 1
        disMode %= 4  # set mode: 0 ~ 3


    

# initialize the IRQs of Pins
modesw.irq(modeSWcb, trigger=Pin.IRQ_FALLING )
setsw.irq(setDownSWcb, trigger=Pin.IRQ_FALLING )


#run timers
dd_tmr=Timer(period=5, mode=Timer.PERIODIC, callback=dd_cb)
halfsectmr=Timer(period=500, mode=Timer.PERIODIC, callback=halfsec_cb)  
