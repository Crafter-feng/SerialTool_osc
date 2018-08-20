

from machine import UART
import sendwave
import urandom
import time

uart = UART(2, baudrate=115200, rx=13,tx=12,timeout=10)

osc = sendwave.SendWave()

for i in range(100):
    value = [urandom.randint(20, 2000) for x in range(16)]
    data = osc.ws_point(*value) 
    #data = osc.ws_sync(*value)        
    uart.write(data)
    time.sleep(0.1)
