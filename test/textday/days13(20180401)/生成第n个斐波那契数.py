#生成斐波那契数，递归方式非常耗时
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(6))



#  使用缓存实现，速度更快
import functools

@functools.lru_cache()   #  注意：必须像常规函数那样调用lru_cache。这一行中有一对括号：@functools.lru_cache()。这么做的原因
                        #         lru_cache可以接受配置参数
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    print(fibonacci(6))