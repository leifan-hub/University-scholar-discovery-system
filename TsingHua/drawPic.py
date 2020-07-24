'''
author:涂珈玮
create time:2020/7/21
update time:2020/7/23

'''

import imageio
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import os
import nature_language_resolve
#import test

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.style.use("ggplot")
isCN = 1 #默认启用中文分词

def drawCloud(i):
    pathA = os.path.abspath('.')
    file = open(pathA + "/Dictionary/" + i + ".txt", mode='r', encoding='utf-8')
    txt = file.read()
    txt = txt.lower()
    index1 = txt.find("图片路径：")
    index2 = txt.find(".jpg")
    txt = txt[0:index1]+txt[index2+4:len(txt)]
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    words = []
    words.extend(i)
    # 将图片作为词云背景
    image_coloring = imageio.imread(pathA + "/white.png")
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='C:\Windows\Fonts\simsun.ttc',
        collocations=False,
        max_words=150,
        min_font_size=5,
        max_font_size=40,
        random_state = 42,
        width = 1000, height = 860, margin = 2,  # 设置图片默认的大小
    )
    mywordlist = []
    seg_list = jieba.cut(txt, cut_all=False)
    liststr = "/ ".join(seg_list)
    f_stop = open(pathA+"/stopWord.txt",encoding = 'utf-8')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1 and i.find(myword.strip()) == -1:
            mywordlist.append(myword)
        if len(mywordlist) == 40:
            break
    if isCN:
       text = ''.join(mywordlist)
    #print(text)
    wc.generate(text)
    plt.figure()
    plt.imshow(image_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.close('all')
    # 保存图片
    wc.to_file(pathA+"/Clouds/"+i+".png")
    file.close()


def drawRose(i, introduction, paper):
    fig = plt.figure(figsize=(12, 10))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location("N")
    pathA = os.path.abspath('.')
    txt = introduction + paper
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    mywordlist = []
    seg_list = jieba.cut(txt, cut_all=False)
    liststr = "/ ".join(seg_list)
    f_stop = open(pathA + "/stopWord.txt", encoding='utf-8')
    text = []
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1 and i.find(myword.strip()) == -1:
            mywordlist.append(myword)
    if isCN:
        text = text + mywordlist
    if len(text) > 10:
        text = text[0:10]
        length = 10
    else:
        length = len(text)
    lenIndex = np.arange(0, length)
    largeIndex = np.arange(2, length + 2)
    theta = np.linspace(1, np.pi * 2, length, endpoint=True)
    # print(text)
    ax.bar(theta, largeIndex, width=0.3, color=np.random.random((len(lenIndex), 3)), align="edge")
    ax.text(np.pi * 3 / 2 - 0.2, 90, "", fontsize=20)
    ax.set_title(i, fontsize=20)
    for angle, height in zip(theta, largeIndex):
        ax.text(angle + 0.03, height, text[height - 2], fontsize=20, color="Black")
    plt.axis('off')
    plt.tight_layout()
    pa = os.path.abspath('.') + "/Roses/" + i + "_rose.png"
    plt.savefig(pa, dpi=480)
    plt.close('all')

