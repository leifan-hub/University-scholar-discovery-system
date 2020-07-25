'''
author:胡志豪
create time:2020/7/15
update time:2020/7/15

'''



import pymysql
import os
import numpy



 

def insertdata(name):
    path='../Crawler/'+name+'.npz'
    data = numpy.load(path, allow_pickle=True)

    db = pymysql.connect("121.199.35.192","root","123456","ssm",charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 插入语句
   

 
    try:  
   # 执行sql语句  
       # cursor.execute(sql)
        cursor.execute('insert into expert(name,school,major,subject,paper,research_direction,introduction) values(%s,%s,%s,%s,%s,%s,%s)',(data['dic'][()]["name"],data['dic'][()]["school"],data['dic'][()]["major"],data['dic'][()]["subject"],data['dic'][()]["paper"],data['dic'][()]["research_direction"],data['dic'][()]["introduction"]))
        cursor.execute('insert into picinfo(name,picurl) values(%s,%s)',(data['dic'][()]["name"],data['dic'][()]["pic"]))
   # 提交到数据库执行
        db.commit()
    except:
   # 如果发生错误则回滚
        db.rollback()
 
# 关闭数据库连接
    db.close()


def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    names=[]
    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.npz':
            names.append(os.path.splitext(i)[0])
    return names

if __name__ == '__main__':
    count=0
    for name in getFileName('../Crawler'):
        count=count+1
        insertdata(name)
       
    print(count)