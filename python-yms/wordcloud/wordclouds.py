"""
Created on Thu Jul 16 12:43:37 2020

@author: 叶茂盛
"""
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:21:40 2020

@author: 32706
"""

def wccre(string,string1):
    img = Image.open(r'background.jpg') 
    img_array = np.array(img)
    stopword=['']
    wc=WordCloud(
    background_color='white',
    width=1000,
    height=800,
    max_words=40,
    mask=img_array, #设置背景图片
    font_path=r'C:\Windows\Fonts\msyh.ttc',
    stopwords=stopword
    )
    wc.generate_from_text(string)
    plt.axis('off')
    plt.show() 
    wc.to_file(r'/%s.png'%(n))
def tcg(texts):
    cut = jieba.cut(texts)  #分词
    string = ' '.join(cut)
    return string
if __name__ == '__main__':
    for i in range(1000,1001):
        path='npz/'+str(i)+'.npz'
        data=np.load(path)
        string=tcg(str(data['paper'])
        wccre(string,data['name'])

     
    
    

