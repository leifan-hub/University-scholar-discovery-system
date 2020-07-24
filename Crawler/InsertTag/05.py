# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from gensim import corpora, models, similarities
from pprint import pprint
import time
import os
import jieba
import MySQLdb


db = MySQLdb.connect(host="121.199.35.192", user="root", password="123456", db="ssm", charset='utf8')
cursor = db.cursor()

if __name__ == '__main__':
    for root, dirs, files in os.walk("D:\\untitled\\info\\"):
        for f in files:
            texts = []
            data = np.load('D:\\untitled\\info\\' + f, allow_pickle=True, encoding='latin1')
            expertList = data['arr_0'][()]
            name = expertList[0]['name']
            text = expertList[0]["research_direction"] + expertList[0]["school"]
            fenci_text = jieba.cut(text)
            stopwords = {}.fromkeys([line.rstrip() for line in open('D:\\untitled\\stopwords.txt', encoding='utf-8')])
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

            num_show_term = 5  # 每个主题显示几个词
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
                print(tags)
                # print('\n概率：\t', term_distribute[:, 1])
                sql = "insert into tag(`name`, `tag`)values('{}','{}')".format(name, tags)
                cursor.execute(sql)
                db.commit()
db.close()



