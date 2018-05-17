#coding=utf-8

import re

ret = re.match(".", "a")
ret.group()

ret = re.match(".", "b")
ret.group()

ret = re.match(".", "M")
ret.group()

#如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello python")
ret.group()



#如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
ret.group()

#大小写h都可以的情况
ret = re.match("[hH]", "Hello Python")
ret.group()

ret = re.match("[hH]", "hello python")
ret.group()

#匹配0到9第一种写法
ret = re.match(r"[0123456789]", "7Hello Python")
ret.group()

#第二种方法
ret = re.match("[0-9]", "7Hello Python")
ret.group()