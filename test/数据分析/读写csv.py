import pandas as pd
#第一种读取方法
df = pd.read_csv('ch06.csv')
print(df)

#第二种读取方法(多加了一个指定分隔符）
print(pd.read_table('ch06.csv', sep=','))
print('-'*50)

df1 = pd.read_csv('ch07.csv', header=None)
print(df1)

print('='*50)

df2 = pd.read_csv('ch07.csv', names=['a', 'b', 'c', 'd', 'message'])
print(df2)


print('='*50)
names=['a', 'b', 'c', 'd', 'message']

df3 = pd.read_csv('ch07.csv', names=names, index_col='message')
print(df3)