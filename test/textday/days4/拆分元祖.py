#如果你想将元祖赋值给类似元祖的变量，python会试图拆分等号右边的值
tup = (4, 5, 6)
a, b, c = tup
print(b)

#即使含有元祖的元祖也会被拆分
tup1 = 4, 5, (6, 7)
a, b, (c, d) = tup1
print(d)

#替换
a, b = 1, 2
print(a, b)
b, a = a, b
print(a, b)