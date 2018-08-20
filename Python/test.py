import sendwave
import random
import time

osc = sendwave.SendWave()
value = [random.randint(20, 2000) for x in range(16)]


data = osc.ws_sync(*value)  
print(data)
data = osc.ws_point(*value)  
print(data)




