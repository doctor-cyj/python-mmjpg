import requests as req
from bs4 import BeautifulSoup
import pymysql, threading, time, configparser

'''多线程类，写入图片下载地址到数据库中'''


class insetIntoAddr(threading.Thread):
    # 传入一个图片网页地址
    def __init__(self, group_picture_addr):
        threading.Thread.__init__(self)
        self.picture_addr = group_picture_addr

    def run(self):
        '''找出最新的一组图片数量'''
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                             "*/*;q=0.8", "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   "Connection": "keep-alive", "Host": "www.mmjpg.com", "Upgrade-Insecure-Requests": "1",
                   "Referer": "http://www.mmjpg.com/mm/",  # 引用地址
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"}
        # print (headers['Referer'])
        # http://www.mmjpg.com/mm/1/1 最后一位是图片数量
        i = 1
        # 这是传入的地址
        url = self.picture_addr
        imgList = []  # 存放图片的地址列表
        while True:
            try:
                tempUrl = url + str(i)
                i += 1
                response = req.get(tempUrl, headers=headers, timeout=20)
                response.encoding = 'utf-8'
                content = response.text
                # 关闭链接对象
                # 判断最大的页数
                if "很抱歉" in content or response.status_code != 200:
                    break
                response.close()
                time.sleep(1)
                soup = BeautifulSoup(content, "html.parser")  # 使用bs库做美味汤
                img_addr = soup.findAll("img")[0]['src']  # 找出图片下载地址
                imgList.append(img_addr)
            except Exception:
                # 需要重复链接下载
                i -= 1

        # 读取数据库链接配置
        conf = configparser.ConfigParser()
        conf.read("mysqlDb.conf", encoding="utf-8")
        db_url = conf.get("MYSQL", "db_url")
        username = conf.get("MYSQL", "user")
        password = conf.get("MYSQL", "password")
        db_name = conf.get("MYSQL", 'db_name')
        # 打开数据库连接
        db = pymysql.connect(db_url, username, password, db_name)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        for temp in imgList:
            # 创建sql 语句，并执行
            sql = "INSERT INTO `img` VALUES (null , '%s')" % (temp)
            try:
                cursor.execute(sql)
                db.commit()
            except Exception:
                db.rollback()
                #当执行SQL语句出错时记录当前的图片下载地址
                with open("error.txt", 'a',encoding='utf-8') as file:
                    file.write(time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime(time.time())) + temp + ":图片下载地址出错了\n")
                file.close()