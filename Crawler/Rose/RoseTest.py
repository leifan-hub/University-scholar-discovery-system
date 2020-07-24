
'''
author:胡志豪
create time:2020/7/15
update time:2020/7/15

'''


import unittest
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import os
import Rose

class Test_RoseTest(unittest.TestCase):
    def test_A(self):
        path='../Rose/安芷生_rose.png'
        self.assertTrue(os.path.exists(path))
    def test_B(self):
        path='../Crawler'
        self.assertIsNotNone(Rose.getFileName(path))
    def test_C(self):
        self.assertIsNotNone(Rose.getdata("安芷生"))
if __name__ == '__main__':
    unittest.main()
