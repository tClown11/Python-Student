import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd='123456789', db="mysql"， charset="utf-8")
cur = conn.cursor()
cur.execute("use scraping")


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())
def store(title, content):
    cur.execute("insert into pages (title, content) values (\"%s\", \"%s\")",(title, content))
    cur.connection.commit()

# https://en.wikipedia.org/wiki/Python_(programming_language)
def getLinks(artcleUrl):
    html = urlopen("http://en.wikipedia.org"+artcleUrl)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()