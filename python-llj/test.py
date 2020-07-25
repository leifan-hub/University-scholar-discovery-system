from typing import List
import jieba
import numpy as np
import jieba.posseg as pseg
import os
import MySQLdb
# 李龙军 雷凡 获取标签第一版

db = MySQLdb.connect(host="121.199.35.192", user="root", password="123456", db="ssm", charset='utf8')
cursor = db.cursor()


def getKeyWords():
    for root, dirs, files in os.walk("/info"):
        # print(files)
        for f in files:
            expert = np.load('/info/'+f, allow_pickle=True, encoding='latin1')
            #print(expert.files)
            expertList = expert['arr_0'][()]
            # print(expertList)
            jieba.load_userdict('/精确词典.txt')
            name = expertList[0]['name']
            text = expertList[0]['research_direction'] + expertList[0]['major']
            words = pseg.cut(text)#text为需要处理的文本
            # words2 = pseg.cut(text)
            # print(expertList[0]['research_direction'])
            # for item in words2:
            #     print(item.word,item.flag)
            compareWords = loadWords()
            flags = ['n', 'nt', 'x', 't']
            tags = ''
            for word in words:
                if word.flag in flags:   #在比对之前先过滤掉分词列表中的非名词
                    for compare_word in compareWords:
                        if compare_word in word.word:
                            tags = tags + word.word + '#'
                            break
            print(tags)
            # sql = "insert into tag(`name`, `tag`)values('{}','{}')".format(name, tags)
            # cursor.execute(sql)
            # db.commit()


def loadWords() -> List[str]:
    with open('/模糊词典.txt', 'r', encoding="utf-8") as f:
        content = f.read().splitlines()
        return content


getKeyWords()
db.close()
