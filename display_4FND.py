# 간단한 4자리 숫자를 다이나믹 구동 방법으로 표시하는 프로그램
# 미리 관련 함수를 만들어 놓은 모듈 (fndControl.py) 이용
#
# @author=senu

import time
import fndControl as fnd


if __name__ == '__main__':
    # #use RTC 
    # rtc = machine.RTC()
    # rtc.datetime([2022,5,9,1,18,50,0,0])
    
    # #toggling 2nd seg's DP to display sec movement
    
    # tmr = Timer(freq=2, mode=Timer.PERIODIC, callback=lambda t: segDP.toggle())
    
    #input the displayed number and check its range
    disnum = int(input('Enter the 4 digits number : '))
    while disnum > 9999 or disnum < 0:
        disnum = int(input('Enter the 4 digits number : '))
    
    now_dis=[disnum//1000, ((disnum%1000)//100), ((disnum%100)//10), (disnum%10) ]
    while True:
        # nowts = rtc.datetime()
        # now_dis = [nowts[4]//10, nowts[4]%10, nowts[5]//10, nowts[5]%10 ]
        
        for i in range(4):
            fnd.displayDigitOne(i,now_dis[i])
            time.sleep_us(fnd.displayRate)
            fnd.turnoffDigit(i)

        