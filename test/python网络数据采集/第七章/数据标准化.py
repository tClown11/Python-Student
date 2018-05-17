# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleanInput(input):
    input = re.sub('\n+', " ", input)     # 把换行符替换成空格
    input = re.sub('\[[0-9]*\]', " ", input)   #剔除[数字]
    input = re.sub(' +', " ", input)    #连续的多个空格替换成空格
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')    #分成单词序列，所有单词按照空格分开
    for item in input:
        item = item.strip(string.punctuation)   #所有的标点符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):  #删除单词a  i
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)   #  分成单词序列，所有单词按照空格分开
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-grams count is:" + str(len(ngrams)))