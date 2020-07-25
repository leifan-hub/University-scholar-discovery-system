'''
author:胡志豪
create time:2020/7/15
update time:2020/7/21

'''



import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import os

def getdata(name):
    #获取数据
    path='../Crawler/'+name+'.npz'
    data = np.load(path, allow_pickle=True)

    #print('....\n',data['dic'][()])
    text=data['dic'][()]["introduction"]+data['dic'][()]["paper"]
    #print(text)
    
    result=jieba.analyse.extract_tags(text,topK=10,withWeight=True)
    
    words=[]
    values=[]
    for tuple in result:
        words.append(tuple[0])
        values.append(tuple[1]*10000+200)
    return words,values,name


def paint(words,values,name):
    theta = np.linspace(0,2*np.pi,len(values))    # 360度等分成n份


    fig = plt.figure(figsize=(15,14))
# 极坐标
    ax = plt.subplot(111,projection = 'polar')
# 顺时针并设置N方向为0度
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')

    ax.bar(theta,
        values,
        width = 0.43,
        color = np.random.random((len(values),3)),
        #labels=str(words), 
        align = 'edge')


    plt.rcParams['font.sans-serif']=['SimHei']  # 黑体
    #ax.set_title('玫瑰图',fontdict={'fontsize':20})
    for angle,data,word in zip(theta,values,words):
        ax.text(angle+0.03,data+105,str(word),fontsize=data/60) 


    plt.axis('off')

    plt.savefig(name+'_rose.png')
   # plt.show()
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
     for name in getFileName('../Crawler'):
        words,values,name=getdata(name)
        paint(words,values,name)
