'''题目描述
描述：

输入一个整数，将这个整数以字符串的形式逆序输出

程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001



输入描述:
输入一个int整数

输出描述:
将这个整数以字符串的形式逆序输出'''

chat = input()
list = []
for i in chat:
    list.append(i)
output = list[::-1]
output = ''.join(output)
print(output)