from machine import Pin
import time

upsw = Pin(0, Pin.IN, Pin.PULL_UP)
dnsw = Pin(1, Pin.IN, Pin.PULL_UP)

led = Pin(25, Pin.OUT)

while True:
    #led.value(upsw.value())
    print('up switch:', upsw.value())
    print('down switch:', dnsw.value())
    time.sleep(1)
