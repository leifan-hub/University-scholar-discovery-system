# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:02:38 2020

@author: 叶茂盛
"""

import numpy as np
import pymysql 
for i in range(1001,1001):
    path='flag/'+str(i)+'.npz'
    data=np.load(path)
 




#2.插入操作 
    db= pymysql.connect(host="121.199.35.192",user="root", password="123456",db="ssm",port=3306)
     
   
# 使用cursor()方法获取操作游标 
    cur = db.cursor()
    sql_insert ="""insert into tag(name,tag) 
values('%s','%s')""" %(data['name'],data['flag'])
   
    
   
    try: 
        cur.execute(sql_insert) 
    #提交 
        db.commit() 
        print('成功插入一条数据')
    
    except Exception as e: 
        print('出错')
        db.rollback()  
    finally: 
        db.close() 