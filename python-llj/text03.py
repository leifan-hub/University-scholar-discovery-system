
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import os
# 李龙军 绘制玫瑰图第二版
for root, dirs, files in os.walk("D:\\untitled\\info\\"):
    #print(files)
    for f in files:
        data = np.load('D:\\untitled\\info\\' + f, allow_pickle=True, encoding='latin1')
        # print(expert.files)
        expertList = data['arr_0'][()]
        name = expertList[0]['name']
        # print('....\n',data['dic'][()])
        text = expertList[0]["introduction"] + expertList[0]["research_direction"] + expertList[0]["school"]
        # print(text)
        result = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
        words = []
        values = []
        for tuple in result:
            words.append(tuple[0])
            values.append(tuple[1] * 10000)
        theta = np.linspace(0, 2 * np.pi, len(values))  # 360度等分成n份
        fig = plt.figure(figsize=(12, 10))
        # 极坐标
        ax = plt.subplot(111, projection='polar')
        # 顺时针并设置N方向为0度
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location('N')

        ax.bar(theta,
               values,
               width=0.43,
               color=np.random.random((len(values), 3)),
               # labels=str(words),
               align='edge')

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
        # ax.set_title('玫瑰图',fontdict={'fontsize':20})
        for angle, data, word in zip(theta, values, words):
            ax.text(angle + 0.03, data + 105, str(word), fontsize=24)

        plt.axis('off')
        #plt.show()
        plt.savefig('D:\\untitled\\_rose\\' + name + '_rose.png')
        print('1')
