# -*- coding : utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    input = re.sub('\n+', " ", input)   #  把换行符替换成空格
    input = re.sub('\[[0-9]*\]', " ", input)   #删除[数字]
    input = re.sub(' +', " ", input)     #连续的多个空格替换成空格
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')    #分成单词序列，所有单词按照空格分开
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == '1'):   #删除单词a i
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramsTemp = " ".join(input[i:i+n])
        if ngramsTemp not in output:
            output[ngramsTemp] = 0
        output[ngramsTemp] += 1
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams)