# SerialTool_osc

SerialTool 是一个非常优秀的串口和网络连接助手，使用Qt编写，可以显示数据波形，还可以跨平台使用，[项目地址](https://github.com/gztss/SerialTool)

* [软件下载地址](https://github.com/gztss/SerialTool/releases/tag/v1.2.4)

快速链接

* [SerialTool-linux64-1.2.3](/SerialTool/SerialTool-linux64-1.2.3.zip)
* [SerialTool1.2.4_Win32_Setup](/SerialTool/SerialTool1.2.4_Win32_Setup.exe)
>注：Linux版本建议使用 [SerialTool-linux64-1.2.3](/SerialTool/SerialTool-linux64-1.2.3.zip)

C语言的用法作者已经写的很详细了，这里我主要说一下如何在microPython环境下使用SerialTool来显示波形

* [使用串口发送数据](##1、使用串口发送数据)
> [test_uart.py](./slave/Python/test_uart.py)

* [使用TCP发送数据](##2、使用TCP发送数据)

> [test_tcp.py](./slave/Python/test_tcp.py)

---

## 1、使用串口发送数据流

### 导入库 
	import sendwave
	from machine import UART
	import urandom	
### 创建对象
	uart = UART(2, baudrate=115200, rx=13,tx=12,timeout=10)
	osc = sendwave.SendWave()

### 生成随机数组
	import urandom
	value = [urandom.randint(20, 2000) for x in range(16)]

### 创建数据流

	data = osc.ws_point(value[1]) 	#点模式,单条数据发送
	data = osc.ws_point(*value) 	#点模式，发送一个长度小于等于16的任意列表

	data = osc.ws_sync(*value) 		#同步模式，发送一个长度小于等于16的任意列表
### 调用串口发送

	uart.write(data)	#发送数据 
	uart.close()

---

## 2、使用TCP发送数据
## 导入库 
	import network
	import socket
	import sendwave
	import urandom	
### 创建对象
	wlan=network.WLAN(network.STA_IF)
	osc = sendwave.SendWave()
	listenSocket = socket.socket()   #创建套接字
### 生成随机数组
	import urandom
   	value = [urandom.randint(20, 2000) for x in range(16)]
### 创建TCP客户端
	port = 10000  #端口号
	ip = wlan.ifconfig()[0]   #获取IP地址
	listenSocket.bind((ip, port))   #绑定地址和端口号
	listenSocket.listen(1)   #监听套接字
	listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #设置套接字
	conn, addr = listenSocket.accept()   #接收连接请求，返回收发数据的套接字对象和客户端地址
### 创建数据流
	data = osc.ws_point(value[1]) 	#点模式,单条数据发送
	data = osc.ws_point(*value) 	#点模式，发送一个长度小于等于16的任意列表

	data = osc.ws_sync(*value) 		#同步模式，发送一个长度小于等于16的任意列表
### 客户端发送
	ret = conn.send(data)   #发送数据
	listenSocket.close() 


