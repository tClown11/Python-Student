#coding = utf-8
__author__ = "keynote"

#利用filter（）过滤出1~100中平方根是整数的数，即结果应该是
#[1, 4, 9, 16, 25, 36, 46, 64, 91, 100]
import math

def is_empty(x):
    return math.sqrt(x)%1 == 0
s = filter(is_empty, range(1, 100))
print(list(s))