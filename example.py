'''

import math

year = int(input("请输入年份： "))

print("year = %d" % (year))

if (year%4)==0 and (year%100)!=0 or (year%400)==0:
    print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)
'''

## 需要说明的是上面代码中的range类型，range可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的
## range(101) 可以产生一个0到100的整数序列。
## range(1, 100) 可以产生一个1到99的整数序列。
## range(1, 100, 2) 可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" % (i,j,i*j),end='\t')
    print()
'''
'''
import math
def main():
    
    j = 0
    print("水仙花分别为：",end = '')
    for i in range(100,1000):
        a = i//100
        b = i%100//10
        c = i%100%10

        if(a**3 + b**3 + c**3 == i):   
            print("%d" % i,end=' ')
            j += 1
    print("水仙花一共有：%d 株" % j)

    pass

if __name__ == '__main__':
    main()
'''
'''
import os
import time

def main():
    content = "贵州欢迎您......"
    t = 20
    while t!=0:
        os.system("cls")
        print(content)
        time.sleep(0.2)  #单位是秒
        content = content[1:] + content[0]#把第一位放在最后一位，每次移动一位0
        t -= 1
    pass

if __name__ == "__main__":
    main()

'''
'''
from time import sleep
import os

class Clock(object):
    def __init__(self,hour = 0,minute = 0,second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    #def hour(self):

    def run(self):
        sleep(1)
        self._second += 1
        if self._second == 60 :
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        return "%02d:%02d:%02d" % (self._hour,self._minute,self._second)   
    pass

def main():
    clock = Clock(23,59,50)
    num = 20
    while num!=0:
        clock.run()
        os.system('cls')
        print(clock.show_time())
        num -= 1
    pass

if __name__ == "__main__":
    main()
'''
#继承
'''
class person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    @property
    def age(aelf):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    
    def play(self):
        print("%s正在愉快的玩耍。" % self._name)

    def watch(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片' % self._name)
        else:
            print('%s正在观看熊出没' % self._name)

class student(person):
    
    def __init__(self,name,age,grade):#表明当前的类有多少的参数
        super().__init__(name,age)#继承person中的name与age
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

def main():
    student1 = student('小红',14,'初三')
    student1.watch()

if __name__ == "__main__":
    main()
'''
#抽象类
'''
from abc import ABCMeta,abstractclassmethod

class pet(object,metaclass=ABCMeta):

    def __init__(self,name):
        self.name = name

    def make_voice(self):
        
        pass
class dog(pet):

    def make_voice(self):
        print('%s:汪汪汪...' % self.name)
class cat(pet):

    def make_voice(self):
        print("%s:喵...喵..." % self.name)

def main():
    pets = [dog('旺财'),cat('小花'),dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == "__main__":
    main()
'''
#tkinter 进行GUI开发
'''
import tkinter
import tkinter.messagebox

def main():
    flag = True

    def chande_lable_text():
        nonlocal flag
        flag = not flag
        color,msg = ('red','Hello world!')\
            if flag else ('blue','Goodbye,world!')
        label.config(text=msg,fg=color)
    
    def confime_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗？'):
            top.quit()

    top = tkinter.Tk()#创建一个对象

    top.geometry('240x160')
    top.title('小游戏')
    label = tkinter.Label(top,text='Hello,world!',font='Arial -32',fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text='修改',command=chande_lable_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='退出',command=confime_to_quit)
    button2.pack(side = 'right')

    panel.pack(side='bottom')
    tkinter.mainloop()

if __name__ == "__main__":
    main()
'''
# 文件操作

'''
f = None
try:    #这样可以进行程序查错
    f = open('F:/procedure_file/python/abc.txt','r',encoding = 'utf-8')
    print(f.read())
except FileExistsError :
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnboundLocalError:
    print('读取文件时解码错误!')
finally:
    if f:
        f.close()
'''
'''
def main():
    f = open('F:/procedure_file/python/abc.txt','r',encoding = 'utf-8')
    print(f.read())
    f.close()


if __name__ == "__main__":
    main()
'''
'''
json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

'''
'''
import json

def main():
    mydict = {
        'name':'罗庚',
        'age':22,
        'qq':1796340734,
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('F:/procedure_file/python/myjson.json','w',encoding = 'utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

    fs = open('F:/procedure_file/python/myjson.json','r',encoding = 'utf-8')
    print(fs.read())
    fs.close()
if __name__ == "__main__":
    main()
'''
# http服务
'''
import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == "__main__":
    main()
'''
# 正则表达式
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
'''
import re 

def main():

    username = input('请输入用户名：')
    qq = input('请输入QQ号：')

    m1 = re.match(r'^[0-9a-zA-Z]\d{6,20}$',username)  #使用了r，表明正则表达式中不会出现转义字符，都是字符本来的意思
    if not m1:
        print('用户名不符合规范.')
    m2 = re.match(r'^[0-9]\d{4,11}$',qq)
    if not m2:
        print('QQ号不符合规范.')
    
    if m1 and m2:
        print('输入信息有效！')

if __name__ == "__main__":
    main()

import re
'''

'''
def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()
'''
# 拆分长字符串
'''
import re

def main():

    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    s_list = re.split(r'[，。，.]',poem)
    print(s_list)
    while '' in s_list:
        s_list.remove('')
    
    print(s_list)

if __name__ == "__main__":
    main()
'''
#进程
'''
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename,time_to_download))

def main():
    start = time()
    p1 = Process(target = download_task, args = ('Python从入门到住院.pdf',))
    p1.start()

    p2 = Process(target = download_task, args = ("Peking Hot.avi",))
    p2.start()
    
    p1.join()
    p2.join()

    end = time()
    print('总共耗费了%.2f秒。' % (end - start))

if __name__ == "__main__":
    main()
'''

# 多线程
'''
from random import randint
from threading import Thread 
from time import time, sleep

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))

def main():

    start = time()
    t1 = Thread(target=download, args=('Python 从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download,args=('Peking Hot.avi',))
    t2.start()
    t1.join()#如果没有这句话，程序会直接往下执行，因为上面两个任务都有相应的 CPU 来运行
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

if __name__ == "__main__":
    main()
'''
'''
#socket 服务器
import socket
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字  

    #print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))

    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('10.16.36.153',6789))
    server.listen(512)

    print('服务器开始监听...')#一般监听的是本机的 IP地址，以及端口
    num = 10
    while num != 0:
        client, addr = server.accept()
        print(str(addr) + '连接服务器.')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()
        num -= 1

if __name__ == '__main__':
    main()
      

'''

import re

def main():
    pat = re.compile(r'[0-9]\d{5}')
    
    string = 'IBT 100012, BUD 234567'

    r = pat.search("IBT 100011")
    print(r.group(0))
    print(pat.split(string, maxsplit = 1))
    print(pat.findall(string )[0])


if __name__ == '__main__':
    main()
        

