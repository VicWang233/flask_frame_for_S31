# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:02:40 2018

@author: VicWang
"""

class data_1():
    def __init__(self,time,datalist):
        self.time = time
        self.datalist = datalist
        self.len = len(self.datalist)
        self.data_frame2_A = []
        self.data_frame2_B = []
        self.data_frame2_C = []
        self.data_frame3 = []
        '''
        #data_1_line：一行数据，格式为列表[名称，数据(None)，行位置，列位置，所在框架]
        data_1_line[4]：根据所在框架分割
        在data_1_line[4] == 2时再次根据data_1_line[3]来分割ABC相
        再根据data_1_line[2]来排序
        '''
    #def split_data_from_frame(self,request):
        for data_1_line in self.datalist:
            if data_1_line[4] == 2:
                if data_1_line[3] == 2:
                    self.data_frame2_A.append(data_1_line)
                elif data_1_line[3] == 3:
                    self.data_frame2_B.append(data_1_line)
                elif data_1_line[3] == 4:
                    self.data_frame2_C.append(data_1_line) 
            elif data_1_line[4] == 3:
                self.data_frame3.append(data_1_line)
        '''排序'''
        self.return_2A = sorted(self.data_frame2_A,key = lambda x:x[2])
        self.return_2B = sorted(self.data_frame2_B,key = lambda x:x[2])
        self.return_2C = sorted(self.data_frame2_C,key = lambda x:x[2])
        self.return_3 = sorted(self.data_frame3,key = lambda x:x[2])
        '''
        根据请求返回响应的列表
        2A：框架2（frame2）A相的值
        2B：框架2（frame2）B相的值
        2C：框架2（frame2）C相的值
        '''
        #if request == '2A':
            #print('self.data_frame2_A',self.return_2A)
        #    return self.return_2A
        #elif request == '2B':
            #print('self.data_frame2_B',self.return_2B)
        #    return self.return_2B
       # elif request == '2C':
            #print('self.data_frame2_C',self.return_2C)
       #     return self.return_2C
       # elif request == '3':
            #print('self.data_frame3',self.return_3)
        #    return self.return_3

#datalist = [('A相12p整流器相电流', None, 24, 2, 2), ('A相6p整流器相电流', None, 23, 2, 2), ('A相输入滤波器电流', None, 22, 2, 2), ('B相12p整流器相电流', None, 24, 3, 2), ('B相6p整流器相电流', None, 23, 3, 2), ('B相输入滤波器电流', None, 22, 3, 2), ('C相12p整流器相电流', None, 24, 4, 2), ('C相6p整流器相电流', None, 23, 4, 2), ('C相输入滤波器电流', None, 22, 4, 2), ('UPS序列号', None, 22, 2, 3), ('整流母线电压', None, 17, 2, 3), ('整流调试变量1', None, 8, 2, 3), ('整流调试变量2', None, 9, 2, 3), ('母线半压', None, 18, 2, 3), ('电感电流', None, 27, 2, 2), ('输出电容电流', None, 28, 2, 2), ('输出视在功率', None, 29, 2, 2), ('逆变母线电压', None, 16, 2, 3), ('逆变相电压', None, 25, 2, 2), ('逆变相电流', None, 26, 2, 2), ('逆变调试变量3', None, 10, 2, 3), ('逆变调试变量4', None, 11, 2, 3)] 
#data = data_1('1',datalist)
#data.split_data_from_frame('3')
