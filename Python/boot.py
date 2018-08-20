
import network
import time    

ssid=''
password=''
    
def connectWifi():
  wlan=network.WLAN(network.STA_IF)                     #create a wlan object
  wlan.active(True)                                     #Activate the network interface
  wlan.connect(ssid,password)   
  i=0
  while(wlan.ifconfig()[0]=='0.0.0.0' and i < 10):
    i=i+1
    time.sleep(1)
  if(wlan.ifconfig()[0]=='0.0.0.0'):
    print('connect Wifi False!')
    return False
  else:
    print('connect Wifi True!')
    print(wlan.ifconfig())
    return True          
if(connectWifi() == True):
  import webrepl
  webrepl.start()

'''
连网以后手动输入这句 ，对webrepl进行初始化！！！

import webrepl_setup
import webrepl_setup
import webrepl_setup

'''

