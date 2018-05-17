from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html, "html.parser")
    nameList = bsObj.findAll("span", {"class" : "red"})
    for name in nameList:
        print(name.get_text())