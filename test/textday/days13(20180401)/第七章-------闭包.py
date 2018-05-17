class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_vlaue):
        self.series.append(new_vlaue)
        total  = sum(self.series)
        return total/len(self.series)

avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))



#方法二
#计算移动平均值的高阶函数
def make_average():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return average    # 注意： 这两个事例的共同之处：调用Avergae（）或make_avergaer（）得到一个可调用对象avg，它会更新历史值，然后计算当前均值

