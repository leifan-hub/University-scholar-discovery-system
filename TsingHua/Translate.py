'''
author:涂珈玮
create time:2020/7/21
update time:2020/7/21

'''

from translate import Translator
import json
from urllib import parse
import http.client
import random
import hashlib

appid = '20200721000523682'  # 你的appid
secretKey = '03NpImRUBz7UqJjVEDY7'  # 你的密钥

def en_Translator(q):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    result = ""
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        # 转码
        html = response.read().decode('utf-8')
        html = json.loads(html)
        dst = html["trans_result"][0]["dst"]
        result = dst
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return result

