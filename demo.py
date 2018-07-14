"""
__author__ = 'Doctor-CYJ'
__mtime__ = '2018/5/3'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from bs4 import BeautifulSoup
import requests, os, time, datetime

starttime = datetime.datetime.now()
# 获取图片页码的总数
url = "http://www.mmjpg.com/"
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                     "*/*;q=0.8", "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
           "Connection": "close", "Host": "www.mmjpg.com", "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"}
# urlList = []  # 放页数的网页地址
# response = requests.get(url, headers=headers)
# response.encoding = "utf-8"
# soup = BeautifulSoup(response.text, "html.parser")
# title = soup.find_all(class_="title")
# print(type(title))
# # print(title)
# # al = list.find_all("a")
# for x in title:
#     urlList.append(x.a['href'])
#
# url = "http://www.mmjpg.com/home/"
# i = 2
# while i <= 90:
#     response = requests.get(url + str(i), headers=headers)
#     response.encoding = "utf-8"
#     soup = BeautifulSoup(response.text, "html.parser")
#     title = soup.find_all(class_="title")
#     # print(type(title))
#     # print(title)
#     for x in title:
#         urlList.append(x.a['href'])
#     i += 1
# print(urlList.__len__())
# with open("url.txt", 'w') as file:
#     for url in urlList:
#         file.write(str(url)+"\n")
# print("写入文件完毕")
# endtime = datetime.datetime.now()
# print(endtime - starttime)
with open("url.txt", 'r') as file:
    line = file.readline()  # 调用文件的 readline()方法
    while line:
        line = line.strip('\n')#自动去掉换行符号
        print(line)
        # print(line, end = '')
        line = file.readline()
