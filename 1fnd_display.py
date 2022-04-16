from machine import Pin
import time

segA=Pin(15,Pin.OUT)
segB=Pin(14,Pin.OUT)
segC=Pin(13,Pin.OUT)
segD=Pin(12,Pin.OUT)
segE=Pin(11,Pin.OUT)
segF=Pin(10,Pin.OUT)
segG=Pin(9,Pin.OUT)

segLst=[segA, segB, segC, segD, segE, segF, segG]

# 0~9 mapping table
segmap = {0:[1,1,1,1,1,1,0], 1:[0,1,1,0,0,0,0], 2:[1,1,0,1,1,0,1],\
          3:[1,1,1,1,0,0,1], 4:[0,1,1,0,0,1,1], 5:[1,0,1,1,0,1,1],\
          6:[1,0,1,1,1,1,1], 7:[1,1,1,0,0,0,0], 8:[1,1,1,1,1,1,1],\
          9:[1,1,1,1,0,1,1], 10:[1,1,1,0,1,1,1], 11:[0,0,1,1,1,1,1],\
          12:[1,0,0,1,1,1,0], 13:[0,1,1,1,1,0,1], 14:[1,0,0,1,1,1,1],\
          15:[1,0,0,0,1,1,1]}

# segA.on()
# time.sleep_ms(500)
# segA.off()
# segB.on()
# time.sleep_ms(500)
# segB.off()
# segC.on()
# time.sleep_ms(500)
# segC.off()
# segD.on()
# time.sleep_ms(500)
# segD.off()
# for i in range(7):
#     segLst[i].on()
#     time.sleep_ms(500)
#           
# for i in range(7):
#     segLst[i].off()
#     time.sleep_ms(500)

#define a function to display one number on 7segments unit
def display_seg(num):
    if num >= 0 and num < 10: #valid range
        mapinfo = segmap[num]
        for i in range(7):
            segLst[i].value(mapinfo[i])
    else:
        mapinfo = segmap['E']
        for i in range(7):
            segLst[i].value(mapinfo[i])

while True:
    for i in range(16):
        #display 1 to 9
        display_seg(i)
        time.sleep(1)