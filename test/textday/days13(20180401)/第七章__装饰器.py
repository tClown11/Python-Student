#装饰器基础知识


'''@decorate
def target():
    print('running target()')
'''


'''#把装饰器通常把函数替换成另一个函数
def deco(func):
    def inner():
        print('running inner()')
    return inner    # deco返回inner函数对象

@deco
def target():   # 使用deco装饰target
    print('running target()')

print(target())    #调用被装饰的target其实会运行inner
print(target)     # 审查target现在是inner的引用
'''

#####装饰器的两大特点是：1.能把被装饰的函数替换成其他函数
#                      2.装饰器在加载模块时立即执行



registry = []     #registry保存被@registry装饰的函数引用

def register(func):    #registry的参数是一个函数
    print('running register(%s)'%func)    # 为了演示，显示被装饰的函数
    register.append(func)    # 把func存入registry
    return func    # 返回func：必须返回函数；这里返回的函数与参数传入的一样

@register    # f1和f2被@registry装饰
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():    #f3没有装饰
    print('running f3()')

def main():     #  main显示registry，然后调用f1（）、f2()、f3()
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()     #只有把registration.py当脚本运行时才调用main()