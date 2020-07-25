'''
author:胡志豪
create time:2020/7/13
update time:2020/7/15

'''



import unittest
import requests
import numpy
from bs4 import BeautifulSoup
import Crawler
#单元测试类
class Test_CrawlerTest(unittest.TestCase):
    def test_A(self):
        urlstart='http://www.xjtu.edu.cn/szdw_lyys.jsp?urltype=tree.TreeTempUrl&wbtreeid=1062'
        self.assertIsNotNone(Crawler.get_content(urlstart))
    def test_B(self):
        urlstart='http://www.xjtu.edu.cn/szdw_lyys.jsp?urltype=tree.TreeTempUrl&wbtreeid=1062'
        content=Crawler.get_content(urlstart)
        html=BeautifulSoup(content, "html.parser")
        
        self.assertEqual(html.head.find("title").text,"两院院士-西安交通大学")
    def test_C(self):
        data = numpy.load('../Crawler/安芷生'+'.npz', allow_pickle=True)
        self.assertEqual("安芷生",data['dic'][()]["name"])
    




if __name__ == '__main__':
    unittest.main()
