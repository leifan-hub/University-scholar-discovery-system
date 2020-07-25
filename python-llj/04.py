
import requests
import numpy as np
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import MySQLdb
import jieba.analyse
import matplotlib.pyplot as plt

# 李龙军 爬取https://www.scimall.org.cn网站学者信息 发现信息缺失 放弃爬取

db = MySQLdb.connect(host="121.199.35.192", user="root", password="123456", db="ssm", charset='utf8')
cursor = db.cursor()

id_2 = 3675

while id_2 < 3803:
    dataDict = {}
    url = "https://www.scimall.org.cn/scholar/detail?id=" + str(id_2)
    id_2 += 1
    r = requests.get(url)
    # r.encoding="utf-8"
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    info1 = soup.find("div", attrs={"class": "user-name"})
    name = str(info1.get_text()).replace("\n", "")
    print(name)
    info2 = soup.find("div", attrs={"class": "user-education"})
    school = info2.get_text()[:45]
    info3 = soup.find("div", attrs={"class": "user-industry"})
    subject = research_direction = major = info3.get_text()
    info4 = soup.find("div", attrs={"class": "user-avator inline-block"})
    url_img = info4.find("img").get('src')
    info5 = soup.find("div", attrs={"class": "info"})
    introduction = info5.get_text()
    info6 = soup.find("ul", attrs={"class": "paper-list"})
    if info6 is None:
        paper = "无"
    else:
        paper = ""
        for i in info6.find_all("li"):
            paper = paper + i.get_text() + '#'

    # dataDict["name"] = name
    # dataDict["school"] = school
    # dataDict["major"] = major
    # dataDict["subject"] = subject
    # dataDict["paper"] = paper
    # dataDict["research_direction"] = research_direction
    # dataDict["introduction"] = introduction
    # data = []
    # data.append(dataDict)
    # np.savez('D:\\untitled\\info2\\' + name, data)
    # data = np.load('D:\\untitled\\info2\\' + name + '.npz', allow_pickle=True, encoding='latin1')
    #
    # text = name + school + paper + research_direction + introduction
    # tags = jieba.analyse.extract_tags(text, 10, withWeight=True)
    #
    # wordcloud = WordCloud(
    #     font_path="C:/Windows/Fonts/simfang.ttf",
    #     max_words=40,
    #     background_color="white", width=1000, height=880).generate(text)
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.savefig('D:\\untitled\\png2\\' + name + ".png")
    print(id_2)
    sql = "insert into expert(`name`, `school`, `major`, `subject`, `paper`, `research_direction`, `introduction`) " \
          "values('{}','{}','{}','{}','{}','{}','{}')".format\
            (name, school, major, subject, paper[:2000], research_direction, introduction[:2000])
    cursor.execute(sql)
    db.commit()
    sql1 = "insert into picinfo(`name`, `picurl`)values('{}','{}')".format(name, url_img)
    cursor.execute(sql1)
    db.commit()
db.close()

