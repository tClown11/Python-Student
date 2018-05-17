# -*- coding : utf-8 -*-
from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))    #随机选取：按照字典中单词频次的权重随机获取一个单词
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    #剔除换行和引号
    text = text.replace("\n", " ")
    text = text.replace("\"", " ")
    #保证每个标点符号都和前面的单词在一起
    #这样不会被剔除，保留在马尔科夫链中
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " "+symbol+" ")

    words = text.split(" ")
    #过滤空单词
    words = [word for word in words if word != ""]
    print(len(words))

    #建一个二维字典---字典有字典 wrod_a -> word_b , word_a -> word_c, word_a -> word_d
    # {word_a : {word_b : 2, word_c : 1, word_d : 1},  表示word_a出现了四次，有2次后面跟word_b 即50%的概率...
    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #为单词新建一个词典
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:  #后一个单词
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]]+ 1
    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
wordDict = buildWordDict(text)
print(len(wordDict))

#生成链长为100的马尔科夫链
length = 100
chian = ""
currentWord = "I"    #以I为开始的句子
for i in range(0, length):
    chian += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])    #  随机选取：按照字典中单词频次的权重随机获取一个单词
print(chian)


#question:items()函数的意思与使用方法
#str的函数调用方法




#生成器、列表解析、迭代器的区别
#迭代器(iterator)

#　　迭代器用来为类序列对象提供一个类序列的接口。迭代器就是生成一个有next()方法的对象，而不是通过索引来计数。

#　　序列、字典、文件中当使用for x in y的结构时，其实质就是迭代器，迭代器是和实际对象绑定在一起的，所以在使用迭代器时或者上述3者时不能修改可变对象的值。反之这会产生错误。如：在使用for x in y的结构来遍历字典时删除符合条件的字典内容，这会导致报错。

#　创建迭代器的方法：iter(object)和iter(func,sentinel)两种。一种使用的是序列，另一种使用类来创建。

#列表解析(List comprehensions)

#　　主要用来动态的创建列表，和map()、filter()和reduce()一样可以用来产生列表。和生成器不同的是，列表解析一次生成一个列表，所占内存较大。

#　　列表解析的扩展版本语法：[expr for iter_var in iterable if cond_expr]

#生成器

#　　生成器是特定的函数，允许你返回一个值，然后“暂停”代码的执行，稍后恢复。生成器使用了“延迟计算”，所以在内存上面更加有效。

#　　生成器表达式：(expr for iter_var in iterable if cond_expr)