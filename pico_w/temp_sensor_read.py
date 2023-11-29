#use internal temperature sensor
#
# senu at 20231115

from machine import Pin
from machine import ADC

import time

brd_led = Pin('LED', Pin.OUT)
temp_sensor = ADC(4)

NoAvg=6
cnt = 0
templst=[]
while True:
    #read temp sensor
    templst.append(temp_sensor.read_u16())
    brd_led.toggle()
    cnt += 1
    if cnt % NoAvg == 0:
    #   print(templst)
        meantemp = sum(templst)/NoAvg
        meantemp = (meantemp* 3.3) / 65535
        temp_degc = 27.0- (meantemp - 0.706) / 0.001721
        print('Temp.: %.2f degC' % temp_degc)
        templst, cnt = [], 0
    
    time.sleep(1)