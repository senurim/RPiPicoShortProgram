import time
import network

ssid='senuOffice2G'
passwd='seulbee67'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, passwd)

#wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() <0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection....')
    time.sleep(1)
    
#handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print(status)