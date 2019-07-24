#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
from urllib.parse import urljoin

import re
import requests

from bs4 import BeautifulSoup


def main():
    headers = {'user-agent': 'Baiduspider'}
    proxies = {
        'http': 'http://122.114.31.177:808'
    }
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    resp = requests.get(seed_url,
                        headers=headers,
                        proxies=proxies)
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    link_set = set()
    for a_tag in soup.find_all('a', {'href': href_regex}):
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
    print('Total %d question pages found.' % len(link_set))


if __name__ == '__main__':
    main()
'''
'''
import requests

def main():

    url = input('请输入需要爬取的网址：')
    # try 语句中，只要出现异常信息，那么就会跳出 try 
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r.text)    

    except:
        print('获取网页信息失败')

if __name__ == "__main__":
    main()

'''
'''
import requests

def main():

    #url = input('请输入爬取网页地址：')
    #keyword = input('请输入关键词：')
    keyword = 'Python'
    try:
        kv = {'wd':keyword}     #
        #kv1 = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get("https://www.so.com/s", params=kv)#, 
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        print(len(r.text))
        #print(r.request.url)
        
        #print(r.text)
    except:
        print('网页爬取异常')

if __name__ == '__main__':
    main()
    
'''
'''
# 图片爬取与保存保存
import requests
import os

def main(): 
    #url = "https://b-ssl.duitang.com/uploads/item/201704/21/20170421083329_3cxt8.png"
    #path = "F:/procedure_file/picture/abc.jpg"
    
    url = input('输入图片的地址：')
    root = "F:/procedure_file/picture/"
    path = root + url.split("/")[-1]

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
            print('文件保存成功')
    except:
        print('爬取信息出错')

if __name__ == '__main__':
    main()
    
'''
'''
import requests
from bs4 import BeautifulSoup

def main():
    url = "http://python123.io/ws/demo.html"
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
        demo = r.text
        soup = BeautifulSoup(demo , "html.parser")
        print(soup.prettify())
        print('成功提取')
    except:
        print('网页信息爬取失败')

if __name__ == '__main__':
    main()
    
'''
from bs4 import BeautifulSoup
import requests

def main():

    url = input('请输入网址：')
    try:
        r = requests.get(url)
        r.raise_for_status()
        demo = r.text

        soup = BeautifulSoup(demo,'html.parser')
        print(soup.title)
    except:
        print('获取信息失败')

if __name__ == '__main__':
    main()




    


    