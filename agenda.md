# 강의 내용 및 순서 / Agenda

2022.04.14
이선우

## 순서
1. 라즈베리파이 피코 보드 소개
  - 공식 문서 페이지 [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
  - [RP2040 MCU](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#welcome-to-rp2040)

2. 소프트웨어 개발 환경 소개
  - C/C++을 사용하여 소프트웨어를 개발하는 방법에 대한 [안내서](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf)
  - 파이썬 언어를 사용하는 방법
    - [Micro Python 소개](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython)
    - RP2를 위한 Micro Python 사용 환경 관련 [안내서](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)

3. Micro Python 사용 환경 만들기 실습
 - 라즈베리파이 공식 문서 [안내서](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
4. 보드 위 LED 제어하기 실습
5. 외부 LED 및 세그먼트 제어하기 실습
6. 스위치 사용 실습  
*7. 4자리수 카운터 만들기 실습 (시간이 되는 경우에만 진행)*

---

## 실습 순서
1. 피코 보드 준비
   1. 마이크로파이썬 실행 파일 다운로드 하기 (uf2 file format)
   2. 피코 보드 USB 메모리 모드로 부팅하기
   3. 파일 복사하기
2. 컴퓨터 준비하기
   1. [Thonny program 설치하기](https://thonny.org/)
   2. 보드 위 LED 제어해보기
3. 7세그먼트 작동하기
   1. 관련 내용 강의
   2. 7세그먼트 - 피코 보드 연결하기
   3. 프로그램 만들기
     - 8개 세그먼트 제어하기
     - 자릿수 (digit) 제어하기
     - 다이나믹 구동 방법 구현하기
4. 버튼 스위치 사용하기
   1. 관련 내용 강의
      - 푸시 버튼 스위치 관련 자료 [코코아팹 자료](https://kocoafab.cc/learn/2)
      - 풀업/풀다운 회로 관련 자료 [위키독스 MSP430](https://wikidocs.net/28690)
      - Contact bounce (also called _chatter_) [Wikipedia](https://en.wikipedia.org/wiki/Switch#Contact_bounce)
      - [Debouncing (채터링 회피 방법) 설명](#푸시-버튼-스위치-채터링-방지-방법-debouncing)
   2. 스위치 2개 보드 연결하기
   3. 프로그램 만들기
      - 스위치 상태 읽어오기
      - 스위치 디바운싱(debouncing) 기법 적용하기
      - 간단 카운터 만들기
5. 4자리수 카운터 만들기

---

## 각 실습별 도움 사이트들
위 실습 순서에 기재된 단계를 수행하는데 도움이 되는 사이트/문서를 정리합니다.

### 1 & 2 단계 : 피코 보드 Micro Pythn 개발 환경  만들기
  
[devicemart 블로그 (따라하기 좋은 문서)](https://devicemart.blogspot.com/2021/06/pc-python.html)

보드 장착 LED 제어하는 코드
  ```python
  led.on() # LED ON 하는 함수. GPIO Pin을 3.3V로 변경.
  # 동일한 결과를 만드는 다른 방법: led.high(),  led.value(1)

  led.off() # LED를 OFF하는 명령어, GPIO Pin 출력을 GND로 변경.
  # 동일 효과:  led.low(), led.value(0)

  led.toggle() #현 상태를 바꾸는 명령어
  ```
관련된 자세한 내용은 [참고문서](https://docs.micropython.org/en/latest/library/machine.Pin.html)를 보자.

### time.sleep() 관련

`time.sleep()` 함수에 대한 도움말도 위 사이트의 [이 페이지](https://docs.micropython.org/en/latest/library/time.html?highlight=sleep#time.sleep)를 참조하자.
  
예제) `time.sleep(1)`: 1초 동안 아무 일도 안하고 기다림.  
      `time.sleep(0.1)`와 같이 실수 값으로도 설정 가능.
        
보다 작은 단위 시간을 사용하는 것도 `time.sleep_ms(ms)` (milisecond 단위로 지정), `time.sleep_us(us)` (micro second 단위로 지정) 함수도 존재

### 푸시 버튼 스위치 채터링 방지 방법 (**debouncing**)
  
- Hardware적인 방법
  - RC Low-pass filter 회로 이용 
    - 장점: 간단한 회로
    - 단점: 느린 응답성
      ![회로도 및 출력 전압 파형](rc_lpf_circuit.png)
         
  - 별도 전용 칩을 사용: [ELM410](https://pdf1.alldatasheet.co.kr/datasheet-pdf/view/142617/ELM/ELM410.html)
- Software적인 방법 
  일정 시간 간격(약 수백ms)을 두고 2번 읽어 동일한 값이면 인정하는 방법
  ```python
    while True:
    #double reading for debouncing
    #check the switch input
    state1= upsw.value() 
    time.sleep_us(100)
    state2= upsw.value()
    if state1 == state2 : #push a button
        if state1 == 0 and onceflag :  #check already count
            onceflag = False
            # action at here!
            # bla bla
        elif state1 == 1:    #no push
            onceflag = True
  ```