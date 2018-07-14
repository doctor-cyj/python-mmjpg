import requests as req, os
from bs4 import BeautifulSoup
import pymysql, time
import myThread,os,random,configparser
'''找出最新的一组图片数量'''
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                     "*/*;q=0.8", "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
           "Connection": "close", "Host": "www.mmjpg.com", "Upgrade-Insecure-Requests": "1",
           "Referer": "http://www.mmjpg.com/",  # 引用地址
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"}
#随机浏览器头
dic = {1:"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        2:"Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
       3:"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
       4:"Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
       5:"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)",
       6:"MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
       7:"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"}
# 获取网站最新的记录
response = req.get("http://www.mmjpg.com/")
response.encoding = "utf-8"  # 设置相应字符编码
soup = BeautifulSoup(response.text, "html.parser")  #
response.close()
liList = soup.findAll("li")  # 找到所有li标签
maxUrl = liList[0].a['href']  # 最新的图片组数量
new_maxNum = maxUrl.split('/')[-1]  # 截取最新的图片组数量
new_maxNum = int(new_maxNum)  # 转换为int类型
# print("网站最新数据是："+str(new_maxNum))
# 查询数据库中最大记录数
#读取数据库链接配置
conf = configparser.ConfigParser()
conf.read("mysqlDb.conf",encoding="utf-8")
db_url = conf.get("MYSQL","db_url")
username = conf.get("MYSQL","user")
password = conf.get("MYSQL","password")
db_name = conf.get("MYSQL",'db_name')
# 打开数据库连接
db = pymysql.connect(db_url, username, password, db_name)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 创建sql 语句，并执行
sql = "select * from max_num"
cursor.execute(sql)
# 获得数据库中的最大记录数
db_max_num = cursor.fetchone()[0]
tempUrl = "http://www.mmjpg.com/mm/"  # 需要拼接的URLhttp://www.mmjpg.com/mm/+maxNum+/
while db_max_num < new_maxNum:
    # print(db_max_num)
    db_max_num +=1 #需要从数据库的数量+1
    url = tempUrl + str(db_max_num) + "/"
    # 开启多线程
    thread1 = myThread.insetIntoAddr(url).run()

# 需要更新数据库的数量
sql = "update max_num set num =%s" % (new_maxNum)
try:
    #更新数据库中最大的图片组数量
    cursor.execute(sql)
    db.commit()
except Exception:
    db.rollback()
finally:
    db.close()
with open("log.txt",'a',encoding='utf-8') as file:
    file.write("当次执行时间是："+time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime(time.time()))+",当前记录数据是:"+str(db_max_num)+'\n')