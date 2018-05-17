'''程序12
题目：判断101-200之间有多少素数，并输出所有素数
程序分析：判断菽粟的方法：用一个数分别去除2到sqrt(这个数)，如果能整除，则表明此数不是素数，反之是素数
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m+1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d'%m,end="")
        h += 1
        if h % 10 == 0:
            print("")
    leap = 1
print("")
print('The total is %d'%h)'''


'''程序13
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位'''
for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if(n == i ** 3 + j ** 3 + k ** 3):
        print("%-5d"% n)