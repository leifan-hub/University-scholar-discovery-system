from typing import List
import jieba
import numpy as np
import jieba.posseg as pseg

#第一版本标签提取代码，后来已弃用

def getKeyWords():
    expert = np.load("../Crawler/陈学俊.npz", allow_pickle=True)
    expertList = expert['dic'][()]
    jieba.load_userdict("精确词典.txt")
    text = expertList['research_direction']
    words = pseg.cut(text)                    #text为需要处理的文本
    words2 = pseg.cut(text)
    print(expertList['research_direction'])
    for item in words2:
        print(item.word,item.flag)
    compareWords = loadWords()
   # for com in compareWords:
    #    print(com)
    #flags = ['n', 'nt', 'x', 't']
    print("123")
    for word in words:
       # if word.flag in flags:   #在比对之前先过滤掉分词列表中的非名词
        for compare_word in compareWords:
            if compare_word in word.word:
                 print(word.word) #这就是提取出来的关键词 word.flag是词性，word.word是词本身
                 break


def loadWords() -> List[str]:
    with open('模糊词典.txt', 'r', encoding="utf-8") as f:
        content = f.read().splitlines()
        return content


getKeyWords()