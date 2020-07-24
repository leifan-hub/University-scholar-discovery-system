'''
author:胡志豪
create time:2020/7/14
update time:2020/7/15

'''



import unittest
import numpy
import WordCloud
import jieba.analyse
import wordcloud
import matplotlib.image as mpimg
#from wordcloud import WordCloud 
import os
#WordCloud单元测试
class Test_WordCloudTest(unittest.TestCase):
    def test_A(self):
        path='../WordCloud/安芷生.png'
        self.assertTrue(os.path.exists(path))
    def test_B(self):
        self.assertIsNotNone(WordCloud.getdata("安芷生"))
    def test_C(self):
        path='../Crawler'
        self.assertIsNotNone(WordCloud.getFileName(path))

if __name__ == '__main__':
    unittest.main()
