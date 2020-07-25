"""
Created on Thu Jul 16 12:43:37 2020

@author: 叶茂盛
"""
import requests
from bs4 import BeautifulSoup
import numpy as np
def func1(str):
    str=str.replace('\t','')
    str=str.replace('\n','')
    str=str.replace('\r','')
    str=str.replace('\xa0','')
    str=str.replace(' ','')
    return str

def func2(str):
    str=str.replace('\t','')
    str=str.replace('\r','')
    str=str.replace('\xa0','')
    str=str.replace(' ','')
    str=str.replace('\n','')
    str=str.replace('.2.','.#2.')
    str=str.replace('.3.','.#3.')
    str=str.replace('.4.','.#4.')
    str=str.replace('.5.','.#5.')
    str=str.replace('.6.','.#6.')
    str=str.replace('.7.','.#7.')
    str=str.replace('.8.','.#8.')
    str=str.replace('.9.','.#9.')
    str=str.replace('.10.','.#10.')
    str=str.replace('；2.','；#2.')
    str=str.replace('；3.','；#3.')
    str=str.replace('；4.','；#4.')
    str=str.replace('；5.','；#5.')
    str=str.replace('；6.','；#6.')
    str=str.replace('；7.','；#7.')
    str=str.replace('；8.','；#8.')
    str=str.replace('；9.','；#9.')
    str=str.replace('；10.','；#10.')                
    return str
def func3(str):
    str=str.replace('院','')
    return str

def __getsinHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    data=requests.get(url,headers=headers).text
    return data
    
    
def __getHtml():
    data=[]
    id=3000
    try:
        while(id < 4000):
            url = "http://db.hbskw.com/pcms/index.php?m=content&c=index&a=show&catid=6&id="+str(id)
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            data.append(requests.get(url,headers=headers).text)
            id+=1

    except Exception as e:
        raise e
    return data

#标志符合条件的学者
def __boolget(html):
    soup = BeautifulSoup(html,"html.parser")
    if soup.find('div',class_='showMsg')==None:
        for div in soup.find_all('div',class_='show_rwsp'):
            if div.find('div',class_='show_bt').text=='代表性论文':
                paper=func1(div.find('p').text) 
                if paper.find('.4.')+paper.find('；4.')>=-1:
                    
                    for div in soup.find_all('div',class_='show_rwsp'):
                        if div.find('div',class_='show_bt').text=='研究方向':
                            for div in soup.find_all('div',class_='show_rwsp'):
                                if div.find('div',class_='show_bt').text=='人物简介':
                                    if soup.find('div', class_='show_yb').find('img'):
                                        return 1
                                                  
    return 0
def __getData(html):
    n=0
    data={}
    soup = BeautifulSoup(html,"html.parser")
    for td in soup.find('div',class_='show_tab').find_all('td'):
        n+=1
        if n==2:
            data['name']=td.text
        if n==4:
            subject = td.text
        if n==8:
            school = td.text
        if n==14:
            major = func3(td.text)
    data['major']=major
    data['school']=school
    data['subject']=subject
    for div in soup.find_all('div',class_='show_rwsp'):
        if div.find('div',class_='show_bt').text=='人物简介':
            data['introduction'] = func1(div.find('p').text )
            
    for div in soup.find_all('div',class_='show_rwsp'):
        if div.find('div',class_='show_bt').text=='研究方向':
            data['research_direction'] = func1(div.find('p').text ) 
                
    for div in soup.find_all('div',class_='show_rwsp'):
        if div.find('div',class_='show_bt').text=='代表性论文':
            data['paper'] = func2(div.find('p').text )                    
    data['img']=soup.find('div', class_='show_yb').find('img')['src']
    return data
if __name__ == '__main__':        
    n=1132
    htmls=__getHtml()
    for i in range(len(htmls)):
        if __boolget(htmls[i])==1:
            data=__getData(htmls[i])
            np.savez(str(n),name=data['name'],school=data['school'],major=data['major'],
                 subject=data['subject'],introduction=data['introduction'],
                 research_direction=data['research_direction'],paper=data['paper'],
                 img=data['img'])
            n+=1
    print('操作成功')

    

