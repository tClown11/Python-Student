global_dict = {}


def std_thread(name):
    std = Student(name)
    #把std放到全局变量global_dict中
    golbal_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    #不传入std，而是根据当前线程查找
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    #任何函数都可以查找出当前线程的std变量
    std = global_dict[threading.current_thread()]
    ...