# 푸시 버튼 스위치 채터링 방지 방법 (debouncing)
  
## Hardware적인 방법
- RC Low-pass filter 회로 이용 
  - 장점: 간단한 회로
  - 단점: 느린 응답성
  ![회로도 및 출력 전압 파형](rc_lpf_circuit.png)
         
- 별도 전용 칩을 사용: [ELM410](https://pdf1.alldatasheet.co.kr/datasheet-pdf/view/142617/ELM/ELM410.html)

## Software적인 방법 
  
### 스텝 1
일정 시간 간격(약 수십ms)을 두고 2번 읽어 동일한 값이면 인정하는 방법

```python
    while True:
    #double reading for debouncing
    #check the switch input
    state1= upsw.value() 
    time.sleep_ms(30)
    state2= upsw.value()
    if state1 == state2 and state1 == 0: #push a button
        # 스위치가 눌렸을 때 필요한 조치를 수행함...
        # 조치 1 
        # 조치 2 
  ```

  ### 스텝 2
  위와 같은 방법으로 스위치 입력을 처리하면 아무 문제가 없나?