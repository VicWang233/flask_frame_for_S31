# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:14:02 2018

@author: VicWang
"""
import time
import sqlite3
from flask import Flask,render_template,request
from models import data_1
import json
'''实例化flask服务器对象'''
app = Flask(__name__)

'''从数据库获取数据的类'''
class get_data_2_sql():
    '''初始化连接数据库'''
    def __init__(self):
        self.conn = sqlite3.connect('C:\\Users\\Administrator\\Desktop\\study\\python\\code\\database_ver.db',check_same_thread = False)
        self.cursor = self.conn.cursor()
    '''获取模拟量数据'''
    def get_analog_quantity(self):
        s = []
        result_41 = self.cursor.execute('SELECT * FROM analogtable_41 ORDER BY name')
        s += list(result_41)
        result_90 = self.cursor.execute('SELECT * FROM analogtable_90 ORDER BY name')
        s += list(result_90)
        result_81 = self.cursor.execute('SELECT * FROM analogtable_81 ORDER BY name')
        s += list(result_81)
        result_82 = self.cursor.execute('SELECT * FROM analogtable_82 ORDER BY name')
        s += list(result_82)
        result_83 = self.cursor.execute('SELECT * FROM analogtable_83 ORDER BY name')
        s += list(result_83)
        #print('S:',list(result_41)+list(result_90)+list(result_81)+list(result_82)+list(result_83))
        return s
    '''获取开关量数据'''
    def get_switching_value(self):
        return list(self.cursor.execute('SELECT * FROM analogtable_switching_name ORDER BY id'))
    '''获取告警量数据'''
    def get_warning_value(self):
        return list(self.cursor.execute('SELECT * FROM analogtable_warning_name ORDER BY id'))
    '''以上为读取，下面为写入,创建表：setting_command，索引：name：值的名称，主键，value：值，status：状态'''
    def set_setting_value(self,data):
        self.data = data
        create_table_setting = '''CREATE TABLE IF NOT EXISTS setting_command (name VARCHA PRIMARY KEY,value VARCHAR,status INTEGER)'''
        self.cursor.execute(create_table_setting)
        try:
            self.cursor.executemany('REPLACE INTO setting_command (name,value,status) VALUES (?,?,?)',[(x[0],x[1],x[2]) for x in self.data])
        except sqlite3.Error as err:
                print("Error occurred in get_switching_value:%s"%err)
        self.conn.commit() 
            
            
            
            
get_data_2_sql = get_data_2_sql()

@app.route('/refresh_analog_quantity')
def refresh_analog_quantity():
    data_frame2_A = []
    data_frame2_B = []
    data_frame2_C = []
    data_frame3 = []
    datalist = get_data_2_sql.get_analog_quantity()
    for data_1_line in datalist:
        if data_1_line[4] == 2:
            if data_1_line[3] == 2:
                data_frame2_A.append(data_1_line)
            elif data_1_line[3] == 3:
                data_frame2_B.append(data_1_line)
            elif data_1_line[3] == 4:
                data_frame2_C.append(data_1_line) 
        elif data_1_line[4] == 3:
            data_frame3.append(data_1_line)
        '''排序'''
        return_2A = sorted(data_frame2_A,key = lambda x:x[2])
        return_2B = sorted(data_frame2_B,key = lambda x:x[2])
        return_2C = sorted(data_frame2_C,key = lambda x:x[2])
        return_3 = sorted(data_frame3,key = lambda x:x[2])
        returnlist = [return_2A,return_2B,return_2C,return_3]
    return json.dumps(returnlist)

@app.route('/refresh_warning_value')
def refresh_warning_value():
    return json.dumps(get_data_2_sql.get_warning_value())
    #return time.strftime('%Y-%m-%d,%H-%M-%S')

@app.route('/refresh_switching_value')
def refresh_switching_value():
    return json.dumps(get_data_2_sql.get_switching_value())


@app.route('/sys_setting')
def refresh_time():
    return render_template('setting.html')

@app.route('/setting',methods=['POST'])
def get_setting_value():
    returnlist = []
    volt_data = request.get_json()['volt']
    returnlist.append(['volt',volt_data,1])
    freq_data = request.get_json()['freq']
    returnlist.append(['freq',freq_data,1])
    get_data_2_sql.set_setting_value(returnlist)
    return json.dumps(returnlist)

@app.route('/test',methods=['POST','GET'])
def test():
    return render_template('test.html',
           data = data_1(time.strftime('%Y-%m-%d,%H-%M-%S')))

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8080,debug = True)