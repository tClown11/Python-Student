#coding=utf-8

#导入re模块
import re

#使用match方法进行匹配操作
#result = re.match(正则表达式， 要匹配的字符串)

#如果上一步匹配数据的话，可以使用group方法来提取数据
#result.group()
'''
re.match是用来进行正则匹配检查的方法，若字符串匹配正则表达式，则match方法返回匹配对象（Match Object），否则返回None（注意不是空字符串""）。

匹配对象Macth Object具有group方法，用来返回字符串的匹配部分。
'''


result = re.match("itcast", "itcast.cn")
result.group()