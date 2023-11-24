# small web server to display the 4bit number
#
# 2023.11.24

import network
import socket
import time
 
from machine import Pin
 
led = Pin(0, Pin.OUT)
 
ssid = 'Sangsangwoorim2.4'
password = 'Lee0927#'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
<head> <title>Pico W</title> </head>
<body> <h1>Pico W</h1>
<p>%s</p>
</body>
</html>
"""

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

#Listen for connection
while True:
    try:
        cl, addr = s.accept()
        print('client connected from ', addr)
        request = cl.recv(1024)
        print(request)
        
        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        
        if led_on == 6:
            print('led on')
            led.on()
            stateis = 'LED is ON'
            
        if led_off == 6:
            print('led off')
            led.off()
            stateis = 'LED is OFF'
            
        response = html % stateis
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')