@d1
@d2
def f():
    print('f')
#等同于
def f():
    print(f)

f = d1(d2(f))


#参数化装饰器
registry = []

def register(func):
    print('running register(%s)' %func)
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

print('running main()')
print('registry ->', registry)
f1()