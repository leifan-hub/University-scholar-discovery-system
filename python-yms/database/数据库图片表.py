# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:10:58 2020

@author: 叶茂盛
"""
import numpy as np
import pymysql 
for i in range(1000,1186):
    path='npz/'+str(i)+'.npz'
    data=np.load(path)
 




#2.插入操作 
    db= pymysql.connect(host="121.199.35.192",user="root", password="123456",db="ssm",port=3306)
     
   
# 使用cursor()方法获取操作游标 
    cur = db.cursor()
    sql_insert ="""insert into picinfo(name,picurl) 
values('%s','%s')""" %(data['name'],data['img'])
   
    
   
    try: 
        cur.execute(sql_insert) 
    #提交 
        db.commit() 
        print('成功插入一条数据')
    
    except Exception as e: 
    #错误回滚 
        db.rollback()  
    finally: 
        db.close() 
  
