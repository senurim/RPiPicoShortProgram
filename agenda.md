# 강의 내용 및 순서 / Agenda

2022.04.14
이선우

### 순서
1. 라즈베리파이 피코 보드 소개
  - 공식 문서 페이지 [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
  - [RP2040 MCU](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#welcome-to-rp2040)

2. 소프트웨어 개발 환경 소개
  - C/C++을 사용하여 소프트웨어를 개발하는 방법에 대한 [안내서](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf)
  - 파이썬 언어를 사용하는 방법
    - [Micro Python 소개](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython)
    - RP2를 위한 Micro Python 사용 환경 관련 [안내서](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)

3. Micro Python 사용 환경 만들기 실습
 - [따라하며 설치하기](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
4. 보드 위 LED 제어하기 실습
5. 외부 LED 및 세그먼트 제어하기 실습
6. 스위치 사용 실습
7. 1자리수 카운터 만들기 실습



### 실습 순서
1. 피코 보드 준비
   1.  마이크로파이썬 실행 파일 다운로드 하기 (uf2 file format)
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
   2. 스위치 2개 보드 연결하기
   3. 프로그램 만들기
      - 스위치 상태 읽어오기
      - 스위치 디바운싱(debouncing) 기법 적용하기
      - 간단 카운터 만들기
5. 4자리수 카운터 만들기


     