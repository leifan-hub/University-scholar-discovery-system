
'''
author:胡志豪
create time:2020/7/14
update time:2020/7/21

'''



import numpy

import jieba.analyse
import wordcloud
import matplotlib.image as mpimg
from wordcloud import WordCloud 
import os

#print(words)

def generate_img(words, img_file,name):
    #生成词云图
    
    datas=' '
    for word in words:
        datas=datas+' '+word
    
    # 将图片作为词云背景
    image_coloring = mpimg.imread(img_file)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='C:\Windows\Fonts\msyh.ttc',
        collocations=False,
        max_words=150,
        min_font_size=5,
        max_font_size=40
    )
    wc.generate(datas)
    wc.to_file(name+'.png')




def getdata(name):
    #获取数据
    path='../Crawler/'+name+'.npz'
    data = numpy.load(path, allow_pickle=True)

    #print('....\n',data['dic'][()])
    text=data['dic'][()]["introduction"]+data['dic'][()]["paper"]
    #print(text)
    words=[]
    word = list(jieba.analyse.extract_tags(text,topK=40))
    #word = list(jieba.analyse.extract_tags(text))
    words.extend(word)
    return words

def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    names=[]
    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.npz':
            names.append(os.path.splitext(i)[0])
    return names




if __name__ == '__main__':
    img_file="456.jpg"
    for name in getFileName('../Crawler'):
        words=getdata(name)
        generate_img(words,img_file,name)
    
   