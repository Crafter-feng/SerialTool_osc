

import struct

class SendWave:
    def __init__(self,Channel_cnt=16,Value_type='Int16'):
        '''
        Oscilloscope 初始化
        SendWave(UART,Channel_cnt=16,Value_type='Int16')
        Channel_cnt         ---开启通道个数，在同步传输的时候会用到
        Value_type          -- 数据类型，Int8，Int16，Int32，Float
        '''
        self.Ch_Num          = Channel_cnt
        self.Frame_Head      = 163      #帧头识别字
        self.Frame_PointMode = 168      #点模式识别字
        self.Frame_SyncMode  = 169      #同步模式识别字
        self.Frame_InfoMode  = 170      #信息帧识别字 
        self.buffer =  []               #数据缓存区 
        self.Format_type = Value_type   #数据格式信息
        
        self.types = {'Int8':(16,'BBBb','Bb'),
                      'Int16':(32,'BBBh','Bh'),
                      'Int32':(48,'BBBi','Bi'),
                      'Float':(0,'BBBf','Bf')}
        self.Format=self.types[self.Format_type][1]
        
    def ws_point(self,*values):
        data = ''
        patten = ''
        Channels = len(values)
        if Channels > 0 and Channels<17:        
            for Channel in range(Channels):
                self.buffer.append(self.Frame_Head)
                self.buffer.append(self.Frame_PointMode)
                self.buffer.append(Channel | self.types[self.Format_type][0]) # 通道及数据格式信息
                self.buffer.append(values[Channel]); # 数据                
            patten = '>'+self.Format*Channels
            data = struct.pack(patten,*self.buffer)
            self.buffer = []
        return data
        
    def ws_sync(self,*values):
        data = ''
        patten = ''
        Channels = len(values)
        
        self.buffer.append(self.Frame_Head)
        self.buffer.append(self.Frame_SyncMode)

        if Channels > 0 and Channels<17:        
            for Channel in range(Channels):
                self.buffer.append(Channel | self.types[self.Format_type][0]) # 通道及数据格式信息            
                self.buffer.append(values[Channel]); # 数据 
            patten = '>'+self.Format+self.types[self.Format_type][2]*(Channels-1)
            data = struct.pack(patten,*self.buffer)
            self.buffer = []
        return data
                
'''        
import sendwave
import random
import time

osc = sendwave.SendWave()
value = [random.randint(20, 2000) for x in range(16)]


data = osc.ws_sync(*value)  
print(data)
data = osc.ws_point(*value)  
print(data)
'''
    
