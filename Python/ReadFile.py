# -*- coding: utf-8 -*-
# ReadFile.py
# @author King
# @description
# @created 2019-06-21T16:42:44.012Z+08:00
# @last-modified 2019-06-21T17:42:18.880Z+08:00
#

import requests
import json


def main():
    f = None
    try:
        f = open('../resources/test.txt', 'r')
        print(f.read())
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def loadsNew():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()
    loadsNew()
