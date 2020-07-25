"""
Created on Thu Jul 16 12:43:37 2020

@author: 叶茂盛
"""
import unittest
import requests
from bs4 import BeautifulSoup
import numpy as np
import scholarResearch
#单元测试类
class Test_CrawlerTest(unittest.TestCase):
    def test_A(self):
        url="http://db.hbskw.com/pcms/index.php?m=content&c=index&a=show&catid=6&id=2674"
        html=scholarResearch.__getsinHtml(url)
        self.assertEqual(scholarResearch.__boolget(html),1,msg="None")


if __name__ == '__main__':
    unittest.main()

