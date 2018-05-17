#自由变量的含义：在A作用域中使用的变量X，却没有在A作用域中声明（即在其他作用域中声明的），对于A作用域来说，X就是一个自由变量


import time

def clock(func):
    def clocked(*args):     #  定义内部函数clocked， 它接受任意个定位参数，返回一个元组
        t0 = time.perf_counter()
        result = func(*args)    #这行代码可用， 是因为clocked的闭包中包含自由变量func
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s) -> %r'% (elapsed, name, arg_str, result))
        return result
    return clocked    #  返回内部函数，取代被装饰的函数


@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == "__main__":
    print('*'*40, 'Calling snooze(.123)')
    snooze(.123)
    print('*'*40, 'Calling factorial(6)')
    print('6! =', factorial(6))