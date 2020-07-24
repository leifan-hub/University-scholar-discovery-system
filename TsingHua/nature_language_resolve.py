'''
author:雷凡
create time:2020/7/13
update time:2020/7/23

'''

from typing import List
import jieba
import numpy as np
import jieba.posseg as pseg
import os

def getKeyWords(i):
    jieba.load_userdict("精确词典.txt")
    text = i
    words = pseg.cut(text)                    #text为需要处理的文本
    words2 = pseg.cut(text)                  #text为需要处理的文本
    print(text)
    for item in words2:
        print(item.word,item.flag)
    compareWords = loadWords()
    finalTag = ""
    flags = ['n', 'nt', 'x', 't']
    num = 0
    for word in words:
        #if word.flag in flags:   #在比对之前先过滤掉分词列表中的非名词
            for compare_word in compareWords:
                if compare_word in word.word:
                    print(word.word) #这就是提取出来的关键词 word.flag是词性，word.word是词本身
                    if finalTag.find(word.word) == -1 and word.word.find("大学"):
                        if num < 3:
                            finalTag = finalTag + word.word + "#"
                            num = num + 1
                    break
    print(finalTag)
    return finalTag


def loadWords() -> List[str]:
    with open('模糊词典.txt', 'r', encoding="utf-8") as f:
        content = f.read().splitlines()
        return content


#getKeyWords("遥感和地理信息的时空数据模型和时空索引、多源数据融合等。")

