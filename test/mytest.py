'''题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
1.程序分析：可填在百位、十位、个位的数字都是、1、2、3、4。组成所有的排序后再去掉不满足条件的排序

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (i != k):
                print(i,j,k)'''

'''题目：企业发放的奖金根据利润提成。利润（I）低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万元到40万元之间是，
高于20万元部分，可提成5%；40万到60万之间，高于40万元的部分，可提成3%；60万到100万之间时高于
60万元的部分，可提成1.5%；高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放
奖金总数？
程序分析：请利用数轴分界，定位。注意定义是需要把奖金定义成长整型
bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.075
bonus4 = bonus2 + 200000 * 0.05
bonus6 = bonus4 + 200000 * 0.03
bonus10 = bonus6 + 400000 * 0.015
i = int(input('input gain:\n'))
if i <= 100000:
    bonus = i * 0.1
elif i <= 200000:
    bonus = bonus1 + (i-100000)*0.075
elif i <= 400000:
    bonus = bonus2 + (i-200000)*0.05
elif i <= 600000:
    bonus = bonus4 + (i-400000)*0.03
elif i <= 1000000:
    bonus =bonus6 + (i-600000)*0.015
else:
    bonus = bonus10 + (i-1000000)*0.01
print('bonus=',bonus)'''


'''程序3
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后在开方如果开方后的结果满足如下条件，
即是结果
import math
for i in range(10000):
    #转化为整型
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x ==i + 100) and (y * y == i + 268):
        print (i)'''


'''程序4
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3
时需考虑多加一天
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if(year % 400 == 0) or ((year % 4 == 0)) and (year % 100 != 0):
    leap = 1
if(leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.'%sum)'''


'''程序5
题目：输入三个整数x,y,z，请把这三个数由小到大输出
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换然后
再用x与z的值进行交换，这样能使x最小
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)'''