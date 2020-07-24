'''
author:涂珈玮
create time:2020/7/21
update time:2020/7/22

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

departmentUrlList = []#取得各院系教师列表
expertUrlList = []#取得单一院系中的教师详情页链接
ua = UserAgent()
headers={"User-Agent":ua.random}
print(headers)


def getDepartmentUrlList():
    r = requests.get("https://home.dartmouth.edu/education/departments-programs-arts-sciences", headers=headers,
                     timeout=30)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text)
    type(soup)
    row = soup.find_all("div",{"class":"row"})
    list = []
    for i in row:
        nine = i.find_all("div", {"class": "nine column"})
        for tag1 in nine:
            pane = tag1.find("div", {"class": "panel-pane pane-node pane-existing-node"})
            panel = pane.find_all("div", {"class": "pane-content"})
            for tag3 in panel:
                p = tag3.find_all('p')
                num = 0
                for tag4 in p:
                    a = tag4.find_all('a')
                    for tag5 in a:
                        urlRaw = tag5.get("href")
                        if urlRaw[len(urlRaw) - 1] != "/":
                            urlRaw = urlRaw + "/"
                        url = urlRaw.replace("academics/undergraduate/", "") + "people"
                        list.append(url)
    for i in list:
        departmentUrlList.append(i)
        if i == "https://sociology.dartmouth.edu/people":
            break

def bridgeFunction1():
    for i in departmentUrlList:
        getExpertUrlList(i)
        time.sleep(5)

def getExpertUrlList(i):
    k = requests.get(i, headers=headers,
                     timeout=30)
    k.encoding = 'utf-8'
    soup = BeautifulSoup(k.text)
    type(soup)
    row = soup.find_all("div",{"class":"row"})
    list = []
    tag = 0
    for tag1 in row:
        twelve = tag1.find_all("div",{"class":"twelve column"})
        for tag2 in twelve:
            if tag == 0:
                view = tag2.find("div", {"class": "view-content"})
                if view != None:
                    ul = view.find("ul", {"class": "people-list clearfix"})
                    # print(ul)
                    for tag3 in ul:
                        if tag3 != None:
                            if tag3.find("li") != -1 and tag3.find("li") != None:
                                a = tag3.find("a")
                                urlRaw = a.get("href")
                                url = i + urlRaw.replace("/people", "")
                                expertUrlList.append(url)
                    tag = 1


def getExpertDetail():
    for i in expertUrlList:
        l = requests.get(i,timeout = 30,headers = headers)
        l.encoding = 'utf-8'
        soup = BeautifulSoup(l.text)
        type(soup)
        expert = {'name':'','school':'达特茅斯大学','major':'','subject':'','paper':'','research_Direction':'','discription':'','img':''}
        four = soup.find("div",{"class":"four columns"})
        bio = four.find("div",{"class":"bio-person-expertise"})
        panel = bio.find("div",{"class":"panel-pane pane-entity-field pane-node-field-people-profile-image"})
        pane = panel.find("div",{"class":"pane-content"})
        pic = pane.find("img")
        expert["img"] = pic.get("src")
        panel = bio.find("div",{"class":"panel-pane pane-entity-field pane-node-field-people-areas-of-expertise"})
        pane = panel.find("div",{"class":"pane-content"})
        p = pane.find("p")
        span = p.find_all("span")
        for sp in span:
            if sp.string.strip() != None:
                directionRaw = sp.string.strip()
                direction = directionRaw
                if directionRaw != "/":
                    direction = Translate.en_Translator(directionRaw)
                expert["research_Direction"] = expert["research_Direction"] + direction
                time.sleep(5)
        eight = soup.find("div",{"class":"bio-main eight columns"})
        panel = eight.find("div",{"class":"panel-pane pane-entity-field pane-node-field-people-selected-pub"})
        pane = panel.find("div",{"class":"pane-content"})
        selected = pane.find("div",{"class":"selected-publications show-more__wrapper"})
        ul = selected.find("ul")
        li = ul.find_all("li")
        for l in li:
            a = l.find("a")
            if a != None:
                expert["paper"] = expert["paper"] +a.string.strip() + "#"
            else:
                p = l.find("p")
                if p.string != None:
                    expert["paper"] = expert["paper"] + p.string.strip() + "#"
        #panelizer = soup.find("div",{"class":"panelizer-view-mode node node-full node-people-profile node-6276"})
        #row = panelizer.find("div",{"class":'row'})
        intro = soup.find("section",{"class":"intro bio"})
        first = intro.find("div",{"class":"first"})
        if first == None:
            first = intro.find("div",{"class":"second"})
        panel = first.find("div",{"class":"panel-pane pane-node-title"})
        pane = panel.find("div",{"class":"pane-content"})
        h1 = pane.find("h1")
        expert["name"] = h1.string.strip()
        statement = intro.find("div",{"class":"intro people__personal-statement"})
        print(statement)
        if statement != None:
            div = statement.find("div")
            span = div.find_all("span")
            num = 0
            for sp in span:
                if sp == None:
                    num = 1
                    break
                else:
                    introRaw = sp.string.strip()
                    intro = Translate.en_Translator(introRaw)
                    expert["discription"] = expert["discription"] + intro
                    time.sleep(5)
            if num == 1:
                p = div.find_all("p")
                for sp in p:
                    if sp != None:
                        introRaw = sp.string.strip()
                        intro = Translate.en_Translator(introRaw)
                        expert["discription"] = expert["discription"] + intro
                        time.sleep(5)
        else:
            statement = intro.find("div",{"class":"intro people__personal-statement show-more__wrapper"})
            div = statement.find("div",{"class":"show-more__default"})
            p = div.find_all("p")
            for sp in p:
                if sp != None:
                   introRaw = sp.string.strip()
                   intro = Translate.en_Translator(introRaw)
                   expert["discription"] = expert["discription"] + intro
                   time.sleep(5)
        h2 = soup.find("h2",{"class":"block-title element-invisible"})
        print(h2)
        major = Translate.en_Translator(h2.string.strip())
        expert["major"] = major
        expert["subject"] = major+"系"
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
        pathA = os.path.abspath('.')
        name = expert["name"]
        pa =pathA+"/Dictionary/"+name+".txt"
        if expert["img"] != "/":
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

def setExpert(i):
    #for i in expertList:
        pathA = os.path.abspath('.')
        expert = {'name':'','school':'达特茅斯大学','major':'','subject':'','paper':'','research_Direction':'','discription':'','img':''}
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

def listTest():
    #for i in departmentUrlList:
     #   print(i)
    for j in expertUrlList:
        print(j)

#getDepartmentUrlList()
#bridgeFunction1()
getExpertUrlList("https://theater.dartmouth.edu/people")#与之前清华大学的原理类似，只能逐一地读取各系的教师主页，否则容易连接超时
getExpertDetail()
listTest()