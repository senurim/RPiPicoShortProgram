# FND 함수를 이용하여 각 자리수를 바꿔가며 0~F까지 표시하는 프로그램
#
# @author = senu

import fndControl as fnd
import time

digitcnt = 0
for i in range(16):
    if digitcnt %2 == 0:
        fnd.displayDigitOne(digitcnt,i, True)
    else: 
        fnd.displayDigitOne(digitcnt,i, False)
    time.sleep(0.7)
    fnd.turnoffDigit(digitcnt)
    digitcnt += 1
    digitcnt %= 4
