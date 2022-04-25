# 인터럽트를 이용한 스위치 입력 처리하기 
#
# Pin.irq() 메소드를 이용하여 스위치 핸들링
#

from machine import Pin
import time

upsw = Pin(0, Pin.IN, Pin.PULL_UP)
dnsw = Pin(1, Pin.IN, Pin.PULL_UP)

countvalue=0

def upSWcb(upsw):
    global countvalue
    countvalue += 1
    if countvalue > 9999: #limit 4 digits
        countvalue = 0

def downSWcb(dnsw):
    global countvalue
    countvalue -= 1
    if countvalue <0:
        countvalue = 9999

upsw.irq(upSWcb, trigger=Pin.IRQ_FALLING )
dnsw.irq(downSWcb, trigger=Pin.IRQ_FALLING )

while True:
    print(countvalue)
    time.sleep(0.5)

