from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#链接上urlopen这个网址
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
#用BeautifulSoup对这个网址进行解析
bsObj = BeautifulSoup(html)

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs)