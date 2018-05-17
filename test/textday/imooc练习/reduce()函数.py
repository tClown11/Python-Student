#coding = utf-8
__author__ = "keynote"

from functools import reduce

#python内置了求和函数sum()，但没有求积的函数， 请利用reduce()来求积：
#输入： [2, 4, 5, 7, 12]
#输出2*4*5*7*12的结果
def prod(x, y):
    #print(x*y)
    return x*y
print(reduce(prod, [2, 4, 5, 7, 12]))
