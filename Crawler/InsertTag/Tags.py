
# -*- coding:utf-8 -*-
#第二版本标签提取代码
import numpy as np
from gensim import corpora, models, similarities
from pprint import pprint
import time
import os
import jieba
import pymysql


db = pymysql.connect(host="121.199.35.192", user="root", password="123456", db="ssm", charset='utf8')
cursor = db.cursor()

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
    
            
            texts = []
            data = np.load('../Crawler/'+name+'.npz', allow_pickle=True)
            expertList = data['dic'][()]
            jieba.load_userdict("精确词典.txt")
            name = expertList['name']
            text = expertList["research_direction"] 
            fenci_text = jieba.cut(text)
            stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords.txt', encoding='utf-8')])
            for word in fenci_text:
                if word not in stopwords and word != " " and word != "，":
                    texts.append([word])
            M = len(texts)
            # 建立字典
            dictionary = corpora.Dictionary(texts)
            V = len(dictionary)
            corpus = [dictionary.doc2bow(text) for text in texts]
            corpus_tfidf = models.TfidfModel(corpus)[corpus]
            # 训练模型
            num_topics = 1
            lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                                  alpha=0.01, eta=0.01, minimum_probability=0.001,
                                  update_every=1, chunksize=100, passes=1)

            num_show_topic = 10  # 每个文档显示前几个主题
            doc_topics = lda.get_document_topics(corpus_tfidf)  # 所有文档的主题分布
            idx = np.arange(M)
            np.random.shuffle(idx)
            idx = idx[:1]
            for i in idx:
                topic = np.array(doc_topics[i])
                topic_distribute = np.array(topic[:, 1])
                # print(topic_distribute)
                topic_idx = topic_distribute.argsort()[:-num_show_topic - 1:-1]
                # print('第%d个文档的前%d个主题：' % (i, num_show_topic)), topic_idx
                # print(topic_distribute[topic_idx])

            num_show_term = 3  # 每个主题显示几个词
            # print('8.结果：每个主题的词分布：--')
            for topic_id in range(num_topics):
                # print('主题#%d：\t' % topic_id)
                term_distribute_all = lda.get_topic_terms(topicid=topic_id)
                term_distribute = term_distribute_all[:num_show_term]
                term_distribute = np.array(term_distribute)
                term_id = term_distribute[:, 0].astype(np.int)
                tags = ""
                # print('词：\t', )
                for t in term_id:
                    # print(dictionary.id2token[t], )
                    tags = tags + dictionary.id2token[t] + '#'
                #print(tags)
              #  print("完成")
                # print('\n概率：\t', term_distribute[:, 1])
          
                cursor.execute('insert into tag(name,tag) values(%s,%s)',(data['dic'][()]["name"],tags))
                db.commit()
db.close()




