

from machine import UART
import sendwave
import urandom
import time

uart = UART(2, baudrate=115200, rx=13,tx=12,timeout=10)
osc = sendwave.SendWave(uart,2)

for i in range(1000):
    value = urandom.randint(20, 2000)
    print(value)
    data = osc.ws_point(0,value)    
    print(data)
    serial.write(data)
    time.sleep(0.1)
