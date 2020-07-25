'''
author:胡志豪
create time:2020/7/13
update time:2020/7/15

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
                      
    rep=requests.get(url)
    rep.encoding = 'utf-8'
      
    return rep.text

def get_data(html_text,picurl):
    #print(html_text)
    final ={}
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    
    
    title=body.find("div",attrs={"class":"pic"})
    tdlist=title.find_all("td")

    final["name"]=tdlist[1].string

    #print(final["name"])
    


    final["school"]="西安交通大学"
   # pic=tdlist[0].find("img",attrs={"id":"personimgid"})
    final["pic"]= 'http://www.xjtu.edu.cn'+picurl
    #print(final["pic"])

    content=body.find_all("div",attrs={"class":"jstext"})
    
    final["research_direction"]=content[1].text
    final["major"]=content[1].text
    final["subject"]=content[1].text
    final["introduction"]=content[2].text
    final["paper"]=content[4].text
    
   # print(final)
           
      
    return final

def write_data(data):
     
   # f = codecs.open(data["name"]+".txt",'w','utf-8')
    name=data["name"]
    
  
    numpy.savez(name,dic=data)
 
    data = numpy.load(name+'.npz', allow_pickle=True)

    #print('....\n',data['dic'][()])
   


if __name__ == '__main__':
    
    sys.setrecursionlimit(1000000)

    
    #爬取西安交通大学的学者信息
   # url ='http://www.xjtu.edu.cn/jsnr.jsp?urltype=tree.TreeTempUrl&wbtreeid=1632&wbwbxjtuteacherid=333'
  #  url1 ='http://www.xjtu.edu.cn/jsnr.jsp?urltype=tree.TreeTempUrl&wbtreeid=1632&wbwbxjtuteacherid=354'
   # html = get_content(url1)
  
   # result = get_data(html)
  #  write_data(result);
    
    urlstart='http://www.xjtu.edu.cn/szdw_lyys.jsp?urltype=tree.TreeTempUrl&wbtreeid=1062'

    index='http://www.xjtu.edu.cn'
    #用urls去保存所有要爬的url
    urls=[]
    rep=requests.get(urlstart)
    rep.encoding = 'utf-8'
    bs = BeautifulSoup(rep.text, "html.parser")
    content=bs.find("div",attrs={"class":"content"})
   # print(bs)
    #print(content)
    for a in bs.find_all("a"):
       # print(a)
        href=a.get('href')
        #用正则表达式来获取所需的全部url
        if re.match(r'^/jsnr+',href):
            path=index+href
          #  print(path)
            urls.append(path)
    #给urls去重并且保留顺序
    urls2=[]
    urls2= sorted(set(urls), key=urls.index)
    urls=urls2
    #print(urls)

    #存储所有专家图片的url
    piclist=[]

    for div in bs.find_all("img"):
    
        piclist.append(div.get('src'))

    del piclist[50:]
    piclist.pop(44)
    del piclist[0:2]
  
    
    '''   
    #不正确的爬取方法，无法获得所有url
    for div in bs.find_all("div",attrs={"class":"lyys"}):
       # print(div)
       # for li in div.find_all("li"):
         #   print(li)
      #  print(div.find("ul"))
        for link in div.find_all("a"):
            #link=li.find("a")
            data=link.get('href')
       # print(data)
        
       # print(path1)
            path=index+data
            print(path)
            urls.append(path)
    '''
    
    index=0
    for link  in urls:
        
        html = get_content(link)
  
        result = get_data(html,piclist[index])
        index=index+1
        write_data(result);
    
