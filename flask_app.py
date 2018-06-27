# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:14:02 2018

@author: VicWang
"""
import time
import sqlite3
from flask import Flask,render_template
from models import data_1

a = ''
app = Flask(__name__)

class get_data_2_sql():
    #初始化连接数据库
    def __init__(self):
        self.conn = sqlite3.connect('C:\\Users\\Administrator\\Desktop\\study\\python\\code\\database_ver.db',check_same_thread = False)
        self.cursor = self.conn.cursor()
    
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
get_data_2_sql = get_data_2_sql()


@app.route('/')
def hello_world():
   return time.strftime('%Y-%m-%d,%H-%M-%S')
@app.route('/test')
def test():
    return render_template('test.html',data = data_1(time.strftime('%Y-%m-%d,%H-%M-%S'),get_data_2_sql.get_analog_quantity()))

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8080,debug = True)