# small web server to display the 4bit number
#
# 2023.11.24

import network
import socket
import time
 
from machine import Pin
 
#HW cofiguration
brdled = Pin('LED', Pin.OUT)
#set the 4 LEDs
led0=Pin(0, Pin.OUT)
led1=Pin(1, Pin.OUT)
led2=Pin(2, Pin.OUT)
led3=Pin(3, Pin.OUT)
 
ssid = 'xxx'
password = 'xxxx'

#display part
display4bit=[led3,led2,led1,led0]

#function for 4bit display
def display(value):
    # masking 4bits
    value &= 0x0F
    for j in range(4):
        if (value>>j) % 2 == 1:
            display4bit[j].on()
        else:
            display4bit[j].off()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
<head> <title>Pico W</title> </head>
<body> <h1>Pico W</h1>
<p>Displayed value is %d</p>
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
    brdled.on()
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    time.sleep(0.1)
    brdled.off()

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
brdled.on()

#Listen for connection
while True:
    try:
        cl, addr = s.accept()
        print('client connected from ', addr)
        request = cl.recv(1024)
        print(request)
        
        request = str(request)
        idx = request.find('/display/')
        #print(idx)
        idx += 9
        value = request[idx:idx+1] 
        print(value)
        value = int(value, 16)
                    
        response = html % value
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
        #display
        display(value)
        
    except OSError as e:
        cl.close()
        print('connection closed')
