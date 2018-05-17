from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
#用BeautifulSoup解析html的网址
bsObj = BeautifulSoup(html)

for link in bsObj.findAll("a"):
    if "href" in link.attrs:
        print(link.attrs['href'])