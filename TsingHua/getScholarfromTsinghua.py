'''
author:涂珈玮
create time:2020/7/13
update time:2020/7/23

'''
import drawPic
import re
import time
import os
import requests
from bs4 import BeautifulSoup
import mysql.connector
from fake_useragent import UserAgent
import Translate
import nature_language_resolve

scholarUrlList = []
urlList = []
#expertList = []
ua = UserAgent()
headers={"User-Agent":ua.random}
print(headers)
r = requests.get("https://thurid.lib.tsinghua.edu.cn/scholar",headers = headers,timeout = 30)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text)
type(soup)

def getScholarUrlList():
    return scholarUrlList
def getUrlList():
    return urlList

def getSchoolPage(soup):#该网页可按首字母搜索专家，该方法的原意是将首字母遍历并于按首字母搜索的网站的的前端整合再存入列表，但本ip疑似受到反爬措施限制，故目前不使用本方法
    ul = soup.find_all("ul",{"class":"clearfix"})
    for data in ul:
        index = data.find_all("a",{"href":"#"})
        for word in index:
            url = "https://thurid.lib.tsinghua.edu.cn/scholar/?color=blue&nameAcronym="+word.string
            urlList.append(url)

def getScholar(soup):
    col = soup.find_all("div",{"class":"col-xs-2"})
    #print(col)
    for data in col:
        a = data.find_all('a')
        for u in a:
            url = u.get("href")
            if url.find("javascript") == -1:
                scholarUrlList.append(url)
                #print(1)
    #return scholarUrlList

def getDetail():
    str = " "
    for word in scholarUrlList:
        i ="https://thurid.lib.tsinghua.edu.cn"+word #目标
        l = requests.get(i,timeout = 30,headers = headers)
        l.encoding = 'utf-8'
        soup = BeautifulSoup(l.text)
        type(soup)
        div1 = soup.find_all("div",{"class":"xzxx"})
        expert = {'name':'','school':'清华大学','major':'','subject':'','paper':'','research_Direction':'','discription':'','img':''}
        for tag1 in div1:
            class1 = tag1.find_all("div",{"class":"col-xs-12 myphoto"})
            for tag2 in class1:
                div2 = tag2.find_all("div",{"class":"row"})
                for tag3 in div2:
                    div3 = tag3.find_all("div",{"class":"myphoto1"})
                    for tag4 in div3:
                        img1 = tag4.find_all('img')
                        for i in img1:
                            imgRaw = i.get("src")
                            if imgRaw.find("jpg") != -1:
                                expert["img"] = "https://thurid.lib.tsinghua.edu.cn"+imgRaw
                            else:
                                expert["img"] = "/"
                    div4 = tag3.find_all("div",{"class":"myphotodivpl"})
                    for tag5 in div4:
                        class2 = tag5.find_all("p",{"class":"realname"})
                        for subjectRaw in class2:
                            for tag6 in subjectRaw:
                                if tag6.find("span") != -1:
                                    if tag6.find("院") != -1:
                                       m = tag6.string[0:len(tag6.string)-1]
                                       subject = m.strip()
                                       expert["subject"] = subject
                                    else:
                                        subject = tag6.string.strip()
                                        expert["subject"] = subject
        div5 = soup.find_all("div",{"class":"myxzjjxz"})
        for tag7 in div5:
            class3 = tag7.find_all("div",{"class":"myxzjj"})
            for tag8 in class3:
                p1 = tag8.find_all("p",{"id":"contain"})
                for discriptionRaw in p1:
                    discription = discriptionRaw.string
                    k = discription
                    expert["discription"] = k
                    if discription.find("主要研究领域：") != -1:
                        dis = discription[discription.find("主要研究领域："):len(discription)]
                        maj = discription[0:discription.find("主要研究领域：")]
                        direction = dis[7:dis.find("。")]
                        expert["research_Direction"] = direction
                        major = ""
                        if maj.find("系") != -1:
                            major = maj[0:maj.find("系")]
                        if maj.find("院") != -1:
                            major = maj[0:maj.find("院")]
                        if maj.find("大学") != -1:
                            major = major[major.find("大学"):len(major)]
                        expert["major"] = major
                    if discription.find("主要研究领域：") == -1 and discription.find("主要研究领域") != -1:
                        dis = discription[discription.find("主要研究领域"):len(discription)]
                        maj = discription[0:discription.find("主要研究领域")]
                        direction = dis[6:dis.find("。")]
                        expert["research_Direction"] = direction
                        if maj.find("系") != -1:
                            major = maj[0:maj.find("系")]
                        if maj.find("院") != -1:
                            major = maj[0:maj.find("院")]
                        if maj.find("大学") != -1:
                            major = major[major.find("大学"):len(major)]
                        expert["major"] = major
                    if discription.find("研究领域：") != -1:
                            dis = discription[discription.find("研究领域："):len(discription)]
                            maj = discription[0:discription.find("研究领域：")]
                            direction = dis[5:dis.find("。")]
                            expert["research_Direction"] = direction
                            if maj.find("系") != -1:
                                i = maj[0:maj.find("系")]
                                major = i.replace(" ", "")
                                expert["major"] = major
                            if maj.find("院") != -1:
                                i = maj[0:maj.find("院")]
                                major = i.strip()
                                expert["major"] = major
                    if discription.find("研究领域：") == -1 and discription.find("研究领域") != -1:
                        dis = discription[discription.find("研究领域"):len(discription)]
                        maj = discription[0:discription.find("研究领域")]
                        direction = dis[4:dis.find("。")]
                        expert["research_Direction"] = direction
                        if maj.find("系") != -1:
                            i = maj[0:maj.find("系")]
                            major = i.replace(" ", "")
                            expert["major"] = major
                        if maj.find("院") != -1:
                            i = maj[0:maj.find("院")]
                            major = i.strip()
                            expert["major"] = major
                    if discription.find("主要研究领域") == -1 and discription.find("研究领域") == -1:
                        if discription.find("系") != -1:
                            major = discription[0:discription.find("系")]
                            expert["major"] = major
                        if discription.find("院") != -1:
                            major = discription[0:discription.find("院")]
                            expert["major"] = major
                if expert["major"] == "":
                    expert["major"] = expert["subject"]
        col = soup.find_all("div",{"class":"col-xs-12 mywzdiv"})
        for c in col:
            data = c.find_all("div", {"class": "col-xs-12"})
            print("--------")
            print("data:")
            print(data)
            print("--------")
            for tr in data:
                print("tr:")
                print(tr)
                print("-------------")
                ltd = tr.find("a",{"target":"_blank"})
                if ltd != None:
                   print(ltd)
                   print("-------------")
                   ta = ltd.string
                   if ta.strip() != "" and ta != None:
                      strT = ta.string
                      if strT.find(".") != -1 and strT.find("More") == -1:
                          print(strT)
                          paperRaw = strT.strip()
                            # print(paperRaw)
                            #paper = Translate.en_Translator(paperRaw)
                            #time.sleep(5)
                            # print(paper)
                          expert["paper"] = expert["paper"] + paperRaw + "#"
        i = expert["paper"]
        expert["paper"] = i[0:len(i)-1]
        div6 = soup.find_all("div",{"class":"col-xs-8 mydqwz"})
        for tag9 in div6:
            a1 = tag9.find_all("a",{"href":word})
            for tag10 in a1:
                expert["name"] = tag10.string
        expert["name"]=expert["name"].strip()
        expert["school"]=expert["school"].strip()
        expert["major"]=expert["major"].strip()
        expert["subject"]=expert["subject"].strip()
        expert["research_Direction"]=expert["research_Direction"].strip()
        expert["discription"]=expert["discription"].strip()
        expert["img"]=expert["img"].strip()
        expert["paper"]=expert["paper"].strip()
        mydb = mysql.connector.connect(
            #host = "localhost",   #便于测试的注释，被注释掉的部分是本机数据库
            host="121.199.35.192",
            port="3306",
            user="root",
            #passwd = "magenstar0",
            passwd="123456",
            database = "ssm",
            charset = "utf8"
        )
        mycursor = mydb.cursor()
        args = expert["name"] + '%'
        sql = "SELECT * FROM expert WHERE name LIKE %s ORDER BY name"
        na = (args,)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        lenExpert = len(myresult)
        sql = "SELECT * FROM picinfo WHERE name LIKE %s ORDER BY name"
        na = (args,)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        lenPic = len(myresult)
        sql = "SELECT * FROM tag WHERE name LIKE %s ORDER BY name"
        na = (args,)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        lenTag = len(myresult)
        if lenExpert != 0 or lenPic != 0 or lenTag != 0:
            expert["name"] = expert["name"] + lenExpert.__str__()
        #expertList.append(expert["name"])
        pathA = os.path.abspath('.')
        name = expert["name"]
        pa =pathA+"/Dictionary/"+name+".txt"
        if expert["img"] != "/" and expert["subject"] != "离退休处" and expert["major"] != "离退休处" and expert["major"] != "" \
                and expert["subject"] != "" and expert["research_Direction"] != "" and expert["discription"] != "" and expert["paper"] != "":
            file = open(pa, mode='w+', encoding='utf-8')
            file.write("姓名：" + expert["name"])
            file.write("\n")
            file.write("学校：" + expert["school"])
            file.write("\n")
            file.write("专业：" + expert["major"])
            file.write("\n")
            file.write("学科：" + expert["subject"])
            file.write("\n")
            file.write("研究方向：" + expert["research_Direction"])
            file.write("\n")
            file.write("简介：" + expert["discription"])
            file.write("\n")
            file.write("图片路径：" + expert["img"])
            file.write("\n")
            print(expert["paper"])
            file.write("论文：" + expert["paper"])
            file.close()
            setExpert(expert["name"])
            time.sleep(5)

def getScholarList(i):
    #for i in urlList:
        k = requests.get(i,timeout = 30,headers = headers)
        time.sleep(5)
        k.encoding = 'utf-8'
        soup = BeautifulSoup(k.text)
        type(soup)
        getScholar(soup)

def setExpert(i):
    #for i in expertList:
        pathA = os.path.abspath('.')
        expert = {'name':'','school':'清华大学','major':'','subject':'','paper':'','research_Direction':'','discription':'','img':''}
        file = open(pathA+"/Dictionary/"+i+".txt",mode = 'r',encoding='utf-8')
        information = file.read()
        nameIndex = information.find("姓名：")
        schoolIndex = information.find("学校：")
        expert["name"] = information[3:schoolIndex].strip()
        majorIndex = information.find("专业：")
        expert["school"] = information[schoolIndex+3:majorIndex].strip()
        subjectIndex = information.find("学科：")
        expert["major"] = information[majorIndex+3:subjectIndex].strip()
        directionIndex = information.find("研究方向：")
        expert["subject"] = information[subjectIndex+3:directionIndex].strip()
        discriptionIndex = information.find("简介：")
        expert["direction"] = information[directionIndex+5:discriptionIndex].strip()
        imgIndex = information.find("图片路径：")
        expert["discription"] = information[discriptionIndex+3:imgIndex].strip()
        paperIndex = information.find("论文：")
        expert["img"] = information[imgIndex+5:paperIndex].strip()
        expert["paper"] = information[paperIndex+3:len(information)].strip()
        tag = nature_language_resolve.getKeyWords(expert["direction"])
        if tag.find("#") == -1:
            tag = expert["major"] + "#" + expert["subject"] + "#"
        mydb = mysql.connector.connect(
            #host = "localhost",
            host="121.199.35.192",
            port="3306",
            user="root",
            #passwd = "magenstar0",
            passwd="123456",
            database = "ssm",
            charset = "utf8"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM expert WHERE name = %s ORDER BY name"
        na = (expert["name"],)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        lenExpert = len(myresult)
        sql = "SELECT * FROM picinfo WHERE name = %s ORDER BY name"
        na = (expert["name"],)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        lenPic = len(myresult)
        sql = "SELECT * FROM tag WHERE name = %s ORDER BY name"
        na = (expert["name"],)
        mycursor.execute(sql, na)
        myresult = mycursor.fetchall()
        lenTag = len(myresult)
        if lenExpert != 0 or lenPic != 0 or lenTag != 0:
            expert["name"] = re.sub(r'\d', "", expert["name"])
            expert["name"] = expert["name"] + lenExpert.__str__()
        sql = "INSERT INTO expert (name, school, major, subject, paper, research_direction, introduction) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (expert["name"],expert["school"],expert["major"],expert["subject"],expert["paper"],expert["direction"],expert["discription"])
        mycursor.execute(sql, val)
        mydb.commit()
        sql1 = "INSERT INTO picinfo (name, picurl) VALUES (%s, %s)"
        val1 = (expert["name"], expert["img"])
        mycursor.execute(sql1, val1)
        mydb.commit()
        sql2 = "INSERT INTO tag (name, tag) VALUES (%s, %s)"
        val2 = (expert["name"], tag)
        mycursor.execute(sql2, val2)
        mydb.commit()
        file.close()
        nature_language_resolve.getKeyWords(i)
        drawPic.drawRose(i,expert["discription"],expert["paper"])
        drawPic.drawCloud(i)



#setExpert("艾海舟")
#print(1)
#getSchoolPage(soup)
getScholarList("https://thurid.lib.tsinghua.edu.cn/scholar/?color=blue&nameAcronym=Z")#由于疑似被反爬虫措施制裁且网络状态不佳
#暂不采取原本的遍历取得网站而是手动将最后的A改为其他其他字母（该网站的结构是按首字母排列专家的）
#只需要把getSchoolPage()的注释取消并把getScholarList()的注释和参数删除即可
getDetail()
#setExpert()

