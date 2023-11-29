import machine
import time
led = machine.Pin('LED', machine.Pin.OUT)
while True:
    led.toggle()
    time.sleep(0.5)
    
    