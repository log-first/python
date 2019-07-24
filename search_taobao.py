import re
from bs4 import BeautifulSoup
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取信息出错！')
        return ''

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # split("...")将一个字符串从 "..." 分开
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

def printGoobsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format("序号", "商品", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goobs = "鞋"
    depth = 3
    str_url = "https://s.taobao.com/search?q=" + goobs
    inforlist = []
    for i in range(depth):
        try:
            url = str_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(inforlist, html)
        except:
            continue
    printGoobsList(inforlist)

if __name__ == '__main__':
    main()



