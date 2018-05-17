#元祖是一个固定长度，不可改变的python序列对象
tup = 4, 5, 6
print(tup)
nested_tup = (4, 5, 6), (7, 8)
print(nested_tup)

#用tuple可以将任意序列或迭代器转换成元祖
print(tuple([4, 5, 6, 7]))

tup = tuple('string')
print(tup)



#可以用括号访问元祖中的元素。。。和C、C++、JAVA等语言一样，序列是从0开始的
print(tup[0])


#如果元祖中某个对象是可变的，比如列表，可以在原位进行修改
tup = tuple(['foo', [1, 2], True])
tup[1].append(3)
print(tup)

#可以用加号运算符将元祖串联起来
tupler = (4, None, 'foo') + (6, 0) + ('bar',)
print(tupler)
#元祖乘以一个整数，像列表一样，会将几个元祖的复制串联起来
tupler1 = ('foo', 'bar') * 4
print(tupler1)
#对象本身没有被复制，只是引用了它