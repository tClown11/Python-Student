#coding = utf-8
def f(x):
    return x*x
v = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#在python3下加你想要的类型，不然就返回内存地址
print(list(v))


#假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map（）函数，把一个list（包含若干不规范的英文名字）
#      变成一个包含规范英文名字的list：输入['adam', 'LISA', 'barT']    输出:['Adam', 'Lisa', 'Bart']

def format_name(a):
    a1 = a[0:1].upper() + a[1:].lower()    #   upper将英文转成大写模式，lower将英文转成小写
    return a1

a2 = map(format_name, ['adam', 'LISA', 'barT'])
print(list(a2))