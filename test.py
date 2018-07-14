import requests as req
from bs4 import BeautifulSoup
import  pymysql,threading,random,os,time
import configparser
'''找出最新的一组图片数量'''
headers = {"Accept": "*/*",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
           "Connection": "close", "Host": "img.mmjpg.com", "Upgrade-Insecure-Requests": "1",
           "Referer": "http://img.mmjpg.com/2018/1341/2",  # 引用地址
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"}
# #生成ConfigParser类对象
# conf = configparser.ConfigParser()
# conf.read("mysqlDb.conf",encoding="utf-8")
# s = conf.get("MYSQL","user")
# print(s)
with open("log.txt",'a',encoding='utf-8') as file :
    file.write(time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime(time.time()))+"当前日期")
