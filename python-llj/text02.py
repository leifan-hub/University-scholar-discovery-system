import requests
from bs4 import BeautifulSoup
from numpy import *
import jieba.analyse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 李龙军 绘制玫瑰图第一版

teacherId = 193

while teacherId < 309:
    teacherId += 1
    if teacherId != 267 and teacherId != 269 and teacherId != 272 and teacherId != 289:
        dataDict = {}
        school = "武汉大学"
        major = "计算机"
        subject = "计算机相关"
        url = "http://cs.whu.edu.cn/teacherinfo.aspx?id="+str(teacherId)
        r = requests.get(url)
        # r.encoding="utf-8"
        soup = BeautifulSoup(r.text, "html.parser")
        info1 = soup.find("ul", attrs={"class": "about_info fn_left"})
        x1 =0
        for i in info1.find_all("li"):
            x1 = x1+1
            j = [s.extract() for s in i('strong')]
            if x1 == 1:
                name = str(i.get_text()).lstrip()
            elif x1 == 9:
                research_direction = i.get_text()
        info2 = soup.find("div", attrs={"id": "myVue"})
        paper = str(info2.find("el-tab-pane", attrs={"label": "发表论文"}).text)[1:2000].replace('\'', '')
        info3 = soup.find("div", attrs={"id": "myVue"})
        introduction = str(info3.find("el-tab-pane", attrs={"label": "研究方向"}).text)[1:2000].replace('\'', '')
        info4 = soup.find("div", attrs={"class": "about_img fn_left"})
        url_p = info4.find("img").get('src')
        if url_p=="":
            url_img='http://cs.whu.edu.cn/images/defaulthead.png'
        else:
            url_img='http://cs.whu.edu.cn'+url_p

        text = research_direction + introduction + paper
        tags = jieba.analyse.extract_tags(text, 8, withWeight=True)
        product_type = []
        sales_num=[]
        for item in tags:
            product_type.append(item[0])
            sales_num.append(round(item[1], 3))
        plt.rcParams['font.sans-serif'] = ['SimHei']
        sn = pd.DataFrame({"关键词": product_type, "比重": sales_num}).sort_values("比重", ascending=False)
        N = 8
        theta = np.linspace(0 + (10 / 180) * np.pi, 2 * np.pi + (10 / 180) * np.pi, N, endpoint=False)
        width = 2 * np.pi / N
        colors = plt.cm.viridis([i for i in np.random.random(N)])
        plt.figure(figsize=(40, 40))
        plt.subplot(111, projection="polar")
        bars = plt.bar(theta, sn["比重"]*80, width=width, bottom=0, color=colors)

        for r, s, t, bar in zip(theta, sn["比重"], sn["关键词"], bars):
            plt.text(r, s*85, str(t) + "\n" + str(s) + "比重", ha="center", va="baseline", fontsize=15)
        plt.axis("off")
        #plt.show()
        plt.savefig('D:\\untitled\\_rose\\'+name+'_rose.png')
        print(teacherId)