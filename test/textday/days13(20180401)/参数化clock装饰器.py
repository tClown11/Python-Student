import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):    #  clock是参数化装饰器工厂函数
    def decorate(func):      #  decorate是真正的装饰器
        def clocked(*_args):   # clocked包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)    #  _result是被装饰的函数返回的真正结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)    #  _args是clocked的参数，args是用于显示的字符串
            result = repr(_result)     #  result是_result的字符串表示形式，用于显示
            print(fmt.format(**locals()))    #  这里使用**locals()是为了在fmt中引用clocked的局部变量
            return _result    #  colcked会取代被装饰的函数，因此它应该返回被装饰的函数返回的值
        return clocked      #   decorate返回clocked
    return decorate       #  clock返回decorate

if __name__ == "__main__":
    @clock()         #    在这个模块中测试，不传入参数调用clock（），因此应用的装饰器使用默认的格式str
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)