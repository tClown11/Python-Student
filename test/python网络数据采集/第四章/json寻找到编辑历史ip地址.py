# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

#获取不会重复的随机数
random.seed(datetime.datetime.now())
#https://en.wikipedia.org/wiki/Python_(programming_language)
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    #编辑历史页面URL链接格式是:
    # https://en.wikipedia.org/w/index.php?title=Python_(programming_language)&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "https://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: "+ historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    #找出class属性是“mw-anonuserlink"的链接
    #它们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList =set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks("/wiki/Python_(programming_language)")

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode("utf-8")
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

while (len(links) > 0 ):
    for link in links:
        print("-"*30)
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            #print(historyIP)
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)
    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)