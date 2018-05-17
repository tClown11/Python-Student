from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime


'''所谓假Random，是指所返回的随机数字其实是一个稳定算法所得出的稳定结果序列，
而不是真正意义上的随机序列。 Seed就是这个算法开始计算的第一个值。所以就会出现
只要seed是一样的，那么后续所有“随机”结果和顺序也都是完全一致的。 通常情况下，
你可以用 DateTime.Now.Millisecend() 也就是当前始终的毫秒来做Seed .因为毫秒对
你来说是一个1000以内的随即数字。 这样可以大大改善保准库的Random结果的随机性。 
不过这仍然算不上是完全随机，因为重复的概率还是千分之一。

另外需要注意的是，如果一直调用标准库Random，那么在调用了N次以后，输出结果就
会循环最开始的序列了。也就是说，标准库Random所能生成的不同结果的个数也是有限
的。32位系统一般也就是几万次以后就会出现重复。'''


#保证random能产生真正的随机数
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)