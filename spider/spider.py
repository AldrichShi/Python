# -*- coding: utf-8 -*-
# spider.py
# @author King
# @description
# @created 2019-07-08T10:29:02.604Z+08:00
# @last-modified 2019-07-08T17:36:28.527Z+08:00
#

import requests
from bs4 import BeautifulSoup
import sys


class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []  # 存放章节名称
        self.urls = []  # 文章下载链接
        self.nums = []  # 文章节数

    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])

        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server+each.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', 'showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')
