# Pico W 강의 내용 및 순서 / Agenda

2023.11.29
이선우

## 순서

1. 부품 배포 & 확인
2. 라즈베리파이 Pico and Pico W 소개
   - 공식 문서 페이지 [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
   - [RP2040 MCU](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#welcome-to-rp2040)

3. 소프트웨어 개발 환경 소개
   - C/C++을 사용하여 소프트웨어를 개발하는 방법: [The C/C++ SDK](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html#sdk-setup)
   - 파이썬 언어를 사용하는 방법
   - [Micro Python 소개](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython)

4. Micro Python 사용 환경 만들기 실습
   - 라즈베리파이 공식 문서 [안내서](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
5. 보드 위 LED 제어하기 실습
6. 외부 LED 및 세그먼트 제어하기 실습
7. 스위치 사용 실습  
*7. 4자리수 카운터 만들기 실습 (시간이 되는 경우에만 진행)*

---

## 실습 순서

1. 부품 확인 및 하드웨어 꾸미기
   1. 확장보드 준비하기
      1. 브레드보드 장착(접착)하기
      2. 피코WH 보드 커넥터에 삽입하고 micro 5 pin USB 케이블 연결하기
      3. 커넥터 (female to female) 이용하여 피코 보드 GPIO와 LED/스위치 연결하기
         1. GP0 - LED1, GP1 - LED2, GP2 - LED3, GP3 - LED4
         2. GP6 - K3 (switch #3), GP7 - K4 (switch #4)
2. 피코 보드 준비
   1. 마이크로파이썬 실행 파일 다운로드 하기 (uf2 file format) [다운로드 사이트 주소](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2)
   2. 피코 보드 USB 메모리 모드로 부팅하기
      1. `BOOTSEL` 스위치를 누른 채로 USB 케이블을 컴퓨터에 연결함
      2. 연결 후 스위치 누르지 않음
   3. 파일 복사하기 (컴퓨터에 새로운 USB메모리를 인식함. 탐색기 등 이용 복사)
3. 컴퓨터 준비하기
   1. [Thonny program 설치하기](https://thonny.org/)
      1. 설치 후 설정하기 : \[Run] 메뉴에서 `Select interpreter...` 선택 후 팝업되는 창에서 `MicroPython (Raspberry Pi Pico)`로 선택함
      2. 아래쪽 `Port` 선택은 `<Try to dectect port automatically >`를 선택함
   ![Thonny option window capture](thonny_option_capture.png)
4. 보드 위 LED 제어해보기
    1. `Thonny` 윈도우의 아래쪽 `Shell` 탭을 이용해 보자. (데모 보면서 따라하기)
    2. 보드 내장 LED 일정 시간 간격으로 깜박이는 프로그램 작성하고 실행하기
```python
from machine import Pin
from time import sleep

brdled=Pin('LED',Pin.OUT) #보드 내장 LED 사용하기 위한 정의

while True: #무한루프
    brdled.toggle() #LED 토글하기
    sleep(0.5)    # 0.5초동안 아무것도 안 하기
```

5. 확장보드 LED 제어하기
    1. 확장보드에는 4개의 청색 LED가 장차되어 있음
    2. 이 4개 LED의 음극(cathode)은 GND에 연결되어 있고 양극(anode)은 피코 보드의 GP0~GP3까지 연결되어 있음
    3. 이 4개 LED를 이용하여 4비트 2진수를 표시하는 디스플레이로 활용 가능
    즉, 0(0b0000) ~ 15(0b1111) 16개 수를 표시할 수 있음

* 0부터 15까지의 2진수를 표시하는 디스플레이 만들기
```python
# simulate the 4-bit counter by using the 4 LEDs on the board
#
# @author = senu
# 20231114
from machine import Pin
import time

#set the 4 LEDs
led0=Pin(0, Pin.OUT)
led1=Pin(1, Pin.OUT)
led2=Pin(2, Pin.OUT)
led3=Pin(3, Pin.OUT)

counter=[led3,led2,led1,led0]

#infinite loop
while True:
    for i in range(16): #couting up from 0 to 15
        #binstr = bin(i)
        for j in range(4):
            if (i>>j) % 2 == 1:
                counter[j].on()
            else:
                counter[j].off()
        time.sleep(0.5)

```
6. 버튼 스위치 사용하기
   1. 관련 내용 강의
      - 푸시 버튼 스위치 관련 자료 [코코아팹 자료](https://kocoafab.cc/learn/2)
      - 풀업/풀다운 회로 관련 자료 [위키독스 MSP430](https://wikidocs.net/28690)
      - Contact bounce (also called *chatter*) [Wikipedia](https://en.wikipedia.org/wiki/Switch#Contact_bounce)
      - [Debouncing (채터링 회피 방법) 설명](#푸시-버튼-스위치-채터링-방지-방법-debouncing)
   2. 스위치 2개 보드 연결하기 (이미 연결되어 있음)
   3. 프로그램 만들기
      - 스위치 상태 읽어오기
      - 스위치 디바운싱(debouncing) 기법 적용하기
      - 간단 카운터 만들기

