'''
author:涂珈玮
create time:2020/7/13
update time:2020/7/15

'''
import os
import time
from typing import List
import jieba
import mysql
import numpy as np
import jieba.posseg as pseg
import unittest

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import getScholarfromTsinghua
import nature_language_resolve
import getExpertFromDartMouth
import Translate

class MyclassTest(unittest.TestCase):
    def test_getScholarList(self):
        url = "https://thurid.lib.tsinghua.edu.cn/scholar/?color=blue&nameAcronym=E"
        getScholarfromTsinghua.getScholarList(url)
        self.assertEqual(len(getScholarfromTsinghua.getScholarUrlList()),8)

    def test_getSchoolPage(self):
        ua = UserAgent()
        headers = {"User-Agent": ua.random}
        print(headers)
        r = requests.get("https://thurid.lib.tsinghua.edu.cn/scholar", headers=headers, timeout=30)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text)
        type(soup)
        getScholarfromTsinghua.getSchoolPage(soup)
        self.assertEqual(len(getScholarfromTsinghua.getUrlList()),26)

    def test_crawlerFile(self):
        path = '/Dictionary/艾海舟.txt'
        pathA = os.path.abspath('.')
        file = open(pathA+path, mode='r', encoding='utf-8')
        information = file.read()
        schoolIndex = information.find("学校：")
        name = information[3:schoolIndex].strip()
        self.assertIsNotNone(name)

    def test_crawlerSQL(self):
        getScholarfromTsinghua.setExpert("艾海舟")
        mydb = mysql.connector.connect(#为避免污染团队的云数据库，此处使用的是本人自身的数据库
            #host = "localhost",
            host="121.199.35.192",
            port="3306",
            user="root",
            #passwd = "magenstar0",
            passwd="123456",
            database = "ssm",
            charset = "utf8"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM expert WHERE name = %s ORDER BY name"
        na = ("艾海舟",)
        print(na)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        mydb.commit()
        #i = "艾海舟" in myresult
        self.assertEqual(len(myresult),1)

    def test_rose(self):
        getScholarfromTsinghua.drawRose("艾海舟","计算机系教授。主要研究领域：计算机视觉与模式识别。获奖：（1）清华大学优秀教学软件二等奖；（2）最佳学生论文奖的指导教师；等。","1.Cross-Resolution Person Re-identification with Deep Antithetical Learning#2.Aggregate Tracklet Appearance Features for Multi-Object Tracking#3.Learning Lightweight Pedestrian Detector with Hierarchical Knowledge Distillation#4.Pedestrian Detection with Central-Line Heatmap Regression#5.FatRegion: A Fast Adaptive Tree-Structured Region Extraction Approach#6.Real-Time Multiple People Tracking with Deeply Learned Candidate Selection and Person Re-Identification#7.Improving pedestrian detection in crowds with synthetic occlusion images#8.Person re-identification with coarse-to-fine visual attention#9.Online multi-object tracking with convolutional neural networks#10.Crowd counting via learning perspective for multi-scale multi-view Web images")
        path='/Roses/艾海舟_rose.png'
        pathA = os.path.abspath('.')
        self.assertTrue(os.path.exists(pathA+path))

    def test_cloud(self):
        getScholarfromTsinghua.drawCloud("艾海舟")
        path='/Clouds/艾海舟.png'
        pathA = os.path.abspath('.')
        self.assertTrue(os.path.exists(pathA+path))

    def test_translate(self):
        a = Translate.en_Translator("I am your father!")
        self.assertEqual(a,"我是你的父亲！")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_getScholarList'))
    suite.addTest(MyclassTest('test_getSchoolPage'))
    suite.addTest(MyclassTest('test_crawlerFile'))
    suite.addTest(MyclassTest('test_crawlerSQL'))
    suite.addTest(MyclassTest('test_rose'))
    suite.addTest(MyclassTest('test_cloud'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

