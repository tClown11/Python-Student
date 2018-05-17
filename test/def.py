'''
def test_add(a,b,c):
    add = a+b
    num = add - c
    print(add)
    print(num)
test_add(21,65,37)
'''
'''
def test_add(num):
    defult = 0
    i = 1
    while i<=num:
        defult+=i
        i+=1
    return defult
num = test_add(100)
print(num)
'''
'''
def num_add(a,b,c):
    return a+b+c
def num_ave(a,b,c):
    defultsum = num_add(a,b,c)
    defultave = defultsum/3
    return defultave
ave = num_ave(12,54,3)
print('输出的平均值是：%d'%ave)
'''
'''输出99乘法表
def calnum(a,b):
    while a<=9:
        test(a,b)
        print("")
        a+=1


def test(a,b):
    while b<=a:
        print("%d*%d=%d\t"%(b,a,a*b),end="")
        b+=1

calnum(1,1)
'''
'''
'用函数实现求100-200的素数'
def sushu(num):
    if num<=200:
        sushu1(num)





def sushu1(num):
    i = 2
    flag = 0
    while i<num:
        if num%i==0:
            i+=1
        else:
'''


def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("不是素数")
            return False
        i += 1
    print("是素数")
    return True
isPrime(105)
'''
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
'''