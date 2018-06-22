'''题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。'''
row = int(input())
words = []  #创建空列表
for i in range(row):  #使用range进行循环次数
    words.append(input()) #添加输入的字符串
words.sort() #由于python中的sort()函数排序后就是以字典排序的形式进行排序，则使用sort()函数即可
for word in words:
    print(word)