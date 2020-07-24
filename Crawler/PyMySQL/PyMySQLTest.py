
'''
author:胡志豪
create time:2020/7/15
update time:2020/7/15

'''

import unittest
import pymysql
import os
import numpy
import PyMySQL
class Test_PyMySQLTest(unittest.TestCase):
    def test_A(self):
        path='../Crawler'
        self.assertIsNotNone(PyMySQL.getFileName(path))
    def test_B(self):
         db = pymysql.connect("121.199.35.192","root","123456","ssm",charset='utf8')
    
         cursor = db.cursor()
         sql='select * from expert where name="安芷生"'
         cursor.execute(sql)  
        
         results = cursor.fetchall()  
         print(results)
         for row in results:  
             id = row[0]  
             name = row[1]
             school = row[2] 
             
             self.assertEqual(school,'西安交通大学')
         db.close()
if __name__ == '__main__':
    unittest.main()
