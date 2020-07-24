'''
author:胡志豪
create time:2020/7/21
update time:2020/7/21

'''


import requests
import csv
import random
import time
import socket
import http.client
import codecs
from bs4 import BeautifulSoup
import numpy
import sys
import re



def get_content(url , data = None):
    #获取html                  
    rep=requests.get(url)
    rep.encoding = 'utf-8'
      
    return rep.text

def get_data(html_text):
    #解析html界面，获取想要的数据
    #print(html_text)
    final ={}
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    
    div1=body.find("div",attrs={"class":"xq_teacher"})
    img=div1.find("img")
    src=img.get('src')
    substr=src[11:]
    if substr=='':
        final["pic"]=''
    else:
        pic='http://cs.bit.edu.cn'+substr
        final["pic"]=pic

    print(final["pic"])
    

    final["school"]="北京理工大学"

    div2=body.find("div",attrs={"class":"bread"})


    links=div2.find_all("a")
    print(links[-1].text)
    final["name"]=links[-1].text


    final["major"]='计算机科学与技术'
    final["subject"]='计算机科学与技术'
   
   

    div3=body.find("div",attrs={"class":"con_teacher"})
    cons=div3.find_all("div",attrs={"class":"con01_t"})

    final["introduction"]=''
    final["research_direction"]=''
    final["paper"]=''


    p1=cons[0].find_all("p")
    
    for p in p1:
        final["introduction"]=final["introduction"]+p.text
    
    if final["introduction"]=='':
        final["introduction"]=cons[0].text
    print(final["introduction"])

    p2=cons[1].find_all("p")
    
    for p in p2:
        final["research_direction"]=final["research_direction"]+p.text
    if final["research_direction"]=='':
        final["research_direction"]=cons[1].text
    
    print(final["research_direction"])
  
    p3=cons[2].find_all("p")
    
    for p in p3:
         final["paper"]=final["paper"]+'#'+p.text
    if final["paper"]=='':
        final["paper"]=cons[2].text
    
    print(final["paper"])
   
           
      
    return final

def write_data(data):
     #把数据写入.npz文件
   # f = codecs.open(data["name"]+".txt",'w','utf-8')
    name=data["name"]
    
  
    numpy.savez(name,dic=data)
 
    data = numpy.load(name+'.npz', allow_pickle=True)

    #print('....\n',data['dic'][()])
   


if __name__ == '__main__':
    
    sys.setrecursionlimit(1000000)

    
    
    urlstart='http://cs.bit.edu.cn/szdw/jsml/index.htm'

    index='http://cs.bit.edu.cn/szdw/jsml/'
    #用urls去保存所有要爬的url
    urls=[]
    rep=requests.get(urlstart)
    rep.encoding = 'utf-8'
    bs = BeautifulSoup(rep.text, "html.parser")
    content=bs.find_all("div",attrs={"class":"teacher"})
   # print(bs)
   # print(content[0])
    for a in content[0].find_all("a"):
        #提取所有要爬取的url
        data=index+a.get('href')
      #  print(data)
        urls.append(data)
  
    urls.pop(3)
    urls.pop(3)
    urls.pop(32)
    for url in urls:

        text=get_content(url)
        data=get_data(text)
        write_data(data)
       
