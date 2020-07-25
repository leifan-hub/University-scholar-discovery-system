# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:43:37 2020

@author: 叶茂盛
"""

import unittest
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import os
import rose

class Test_RoseTest(unittest.TestCase):
#袁银传图片是否存在
    def test_A(self):
        path='../rose/袁银传_rose.png'
        self.assertTrue(os.path.exists(path))
#袁银传数据是否存在
    def test_B(self):
        path='../rose/npz/1000.npz'
        self.assertIsNotNone(os.path.exists(path))

if __name__ == '__main__':
    unittest.main()