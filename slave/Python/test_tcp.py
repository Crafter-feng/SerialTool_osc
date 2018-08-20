import network
import socket
import time
import sendwave
import urandom


port = 10000  #端口号
wlan = None  #wlan
listenSocket = None  #套接字

osc = sendwave.SendWave()

try:
  wlan=network.WLAN(network.STA_IF)
  ip = wlan.ifconfig()[0]   #获取IP地址
  listenSocket = socket.socket()   #创建套接字
  listenSocket.bind((ip, port))   #绑定地址和端口号
  listenSocket.listen(1)   #监听套接字
  listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #设置套接字
  print ('tcp waiting...')

  while True:
    print("accepting.....")
    conn, addr = listenSocket.accept()   #接收连接请求，返回收发数据的套接字对象和客户端地址
    print(addr, "connected")
    while True:      
      value = [urandom.randint(20, 2000) for x in range(16)]
      data = osc.ws_point(*value)  
      ret = conn.send(data)   #发送数据      
      time.sleep(0.1)      
      
except:
  if(listenSocket):   #判断套接字是否为空
    listenSocket.close()   #关闭套接字

