# -*- coding: utf - 8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

#获取页面所有内链接的列表
def getInternalLinks(bsObj, incldeUrl):
    internalLinks = []
    #找出所有有以“/”开头的链接
    #for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
    for link in bsObj.findAll("a", href=re.compile("^(/)")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #找出所有以“http”或“www”开头并不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def printAllLinks(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])
#printAllLinks("http://oreilly.com")

#收集网站上发现的所有外链列表
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            print("即将获取的链接的URL是：" + link)
            allExtLinks.add(link)
            getAllExternalLinks(link)

    for link in internalLinks:
        if link not in allIntLinks:
            print(link)
            allIntLinks.add(link)

#getAllExternalLinks("http://oreilly.com")
getAllExternalLinks("http://www.pku.edu.cn")