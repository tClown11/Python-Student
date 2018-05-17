#在 Python 3.x 版本中, urllib.request.urlretrieve 可以根据文件的 URL 下载文件:
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a", {"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")


