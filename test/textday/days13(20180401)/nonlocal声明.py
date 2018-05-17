#计算移动平均值得高阶函数，不保存所有历史值，但有缺陷
def make_averager():
    count = 0
    total = 0
    print(count)

    def averager(new_value):
        nonlocal count, total   #   noncal的作用是吧变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量
        count += 1
        total += new_value
        print(count)
        return total/count
    return averager
avg = make_averager()
print(avg(10))
print(avg(15))
