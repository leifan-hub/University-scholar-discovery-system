"""
Created on Thu Jul 16 12:43:37 2020

@author: 叶茂盛
"""
# -*- coding: utf-8 -*-


import unittest
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import os
import wordcloud

class Test_RoseTest(unittest.TestCase):
#袁银传图片是否存在
    def test_A(self):
        path='../wordcloud/袁银传.png'
        self.assertTrue(os.path.exists(path))
#袁银传数据是否存在
    def test_B(self):
        path='../wordcloud/npz/1000.npz'
        self.assertIsNotNone(os.path.exists(path))

if __name__ == '__main__':
    unittest.main()