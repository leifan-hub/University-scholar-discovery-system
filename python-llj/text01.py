import requests
import numpy as np
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import MySQLdb
import jieba.analyse
import matplotlib.pyplot as plt
# 李龙军 爬取武大计算机学院学者信息

db = MySQLdb.connect(host="121.199.35.192", user="root", password="123456", db="ssm", charset='utf8')
cursor = db.cursor()

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
            elif x1 == 4:
                zhiwei = i.get_text()
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

        # dataDict["name"] = name
        # dataDict["school"] = school
        # dataDict["major"] = major
        # dataDict["subject"] = subject
        # dataDict["paper"] = paper
        # dataDict["research_direction"] = research_direction
        # dataDict["introduction"] = introduction
        # dataDict["zhiwei"] = zhiwei
        # data = []
        # data.append(dataDict)
        # np.savez('D:\\untitled\\info\\' + name, data)
        # data = np.load('D:\\untitled\\info\\' + name + '.npz', allow_pickle=True, encoding='latin1')
        #
        # text = name + school + major + subject + paper + research_direction + introduction + zhiwei
        # tags = jieba.analyse.extract_tags(text, 10, withWeight=True)
        #
        # wordcloud = WordCloud(
        #     font_path="C:/Windows/Fonts/simfang.ttf",
        #     max_words=40,
        #     background_color="white", width=1000, height=880).generate(text)
        # plt.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        # plt.savefig('D:\\untitled\\png\\' + name + ".png")

        # data = np.load('D:\\untitled\\info\\' + name + '.npz', allow_pickle=True, encoding='latin1')
        # print(data['arr_0'])
        sql = "insert into expert(`name`, `school`, `major`, `subject`, `paper`, `research_direction`, `introduction`) " \
              "values('{}','{}','{}','{}','{}','{}','{}')".format\
                (name, school, major, subject, paper, research_direction, introduction)
        cursor.execute(sql)
        db.commit()
        sql1 = "insert into picinfo(`name`, `picurl`)values('{}','{}')".format(name, url_img)
        cursor.execute(sql1)
        db.commit()
        print(teacherId)
db.close()
#
# def getnpz():
#     dataDict["name"] = name
#     dataDict["school"] = school
#     dataDict["major"] = major
#     dataDict["subject"] = subject
#     dataDict["paper"] = paper
#     dataDict["research_direction"] = research_direction
#     dataDict["introduction"] = introduction
#     dataDict["zhiwei"] = zhiwei
#     data = []
#     data.append(dataDict)
#     np.savez('D:\\untitled\\info\\' + name, data)
#     data = np.load('D:\\untitled\\info\\' + name + '.npz', allow_pickle=True, encoding='latin1')
#
#     text = name + school + major + subject + paper + research_direction + introduction +zhiwei
#     tags = jieba.analyse.extract_tags(text, 10, withWeight=True)
#
#     wordcloud = WordCloud(
#         font_path="C:/Windows/Fonts/simfang.ttf",
#         max_words=40,
#         background_color="white", width=1000, height=880).generate(text)
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.savefig('D:\\untitled\\png\\' + name + ".png")

