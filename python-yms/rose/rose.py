# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:43:37 2020

@author: 叶茂盛
"""
import  jieba
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl  

mpl.rcParams['font.sans-serif'] = ['SimHei'] 

   # 使用精确模式对文本进行分词




for i in range(1000,1001):
    tx=[]
    num=[]
    counts = {}
    n=0
    path='npz/'+str(i)+'.npz'
    data=np.load(path)
    string=str(data['paper'])
    words = jieba.lcut(string)  
    for word in words:
        if  len(word) == 1:    # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
        
    items = list(counts.items())#将键值对转换成列表
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

    for i in range(10):
        word, count = items[i]
        tx.append(word)
        num.append(count*50+100)
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    theta = np.linspace(0, np.pi*2, 10, endpoint=False)
    ax.bar(theta, num, width=0.4,
       color=np.random.random((len(num),3)),
       align='edge',
       bottom=20)

    


    for angle, height in zip(theta,num):
        ax.text(angle+0.03, height+50, tx[n], 
            fontsize=height/14)
        n+=1

    plt.axis('off')
    plt.tight_layout()
    path=r'%s_rose.png'%(data['name'])
    plt.savefig(path, dpi=100)

