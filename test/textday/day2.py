import numpy as np

'''
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)#randn是从正态分布中返回一个或多个值‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’
#rand则是随机样本位于（0， 1）中
print(names)
print('---------------')
print(data)
print('---------------')
print(names == "Bob")
print('---------------')
print(data[names == 'Bob'])
print('---------------')
print(data[names == 'Bob', 2:])
print('---------------')
print(data[names == 'Bob', 3])
print('---------------')
print(names != 'Bob')
print('---------------')
print(data[~ (names == 'Bob')])
print('---------------')
mask = (names == "Bob")|(names == "Will")
print(mask)
print('---------------')
print(data[mask])
print('---------------')
data[data < 0] = 0
print(data)
print('---------------')
data[names != 'Joe'] = 7
print(data)
'''
'''
#花式索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
print('---------------')
#为了以特定顺序选取行子集，只需传入一个用于指定顺序的整数列表或ndarray即可
print(arr[[4, 3, 0, 6]])
print('---------------')
#使用负数索引将会从末尾开始选取行
print(arr[[-3, -5, -7]])
print('---------------')
'''

arr = np.arange(32).reshape((8, 4))
print(arr)
print('---------------')
print(arr[[1, 5, 7, 2],[0, 3, 1, 2]])