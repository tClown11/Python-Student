'''程序6
题目：用‘*’号在纸上写出字母C，再分行输出
print('Hello Python world!\n')
print('*'*10)
for i in range(5):
    print('*   *')
print('*'* 10)'''


'''程序7
题目：输出特殊图案，请在c环境中运行，看一看
字符共有256个。不同字符，图形不一样
a = 176
b = 219
print(chr(b),chr(a),chr(a),chr(a),chr(b))
print(chr(a),chr(b),chr(a),chr(b),chr(a))
print(chr(a),chr(a),chr(b),chr(a),chr(a))
print(chr(a),chr(b),chr(a),chr(b),chr(a))
print(chr(b),chr(a),chr(a),chr(a),chr(b))'''



'''程序8
题目：输出9*9口诀
程序分析：分行与列考虑，共9行9列，i控制行，j控制列
for i in range(1,10):
    for j in range(1,i+1):
        result = i * j
        print('%d*%d = %-4d'%(i,j,result),end = '')#-4d表示左对齐，占4位
    print('')'''



'''程序9
题目：要求输出国际象棋棋盘
程序分析：用i控制行，j控制列，根据i+j的和的变化来控制输出黑方格，还是白方格
import sys
for i in range(8):
    for j in range(8):
        if((i + j)% 2 == 0):
            sys.stdout.write(chr(220))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write('')
    print('')'''



'''程序10
题目：古典问题：有一对兔子，从出生后第三个月期每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1，1，2，3，5，8，13，21...
f1 = 1
f2 = 1
for i in range(1,21):
    print('%12d%12d'%(f1,f2))
    if((i%2) == 0):
        print('')
    f1 = f1 + f2
    f2 = f1 + f2
'''