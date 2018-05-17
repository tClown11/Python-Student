import threading
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写子集线程的独立副本，互不干扰。
#ThreadLocal解决了参数在一个线程中各个函数之间相互传递的问题



#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('tanjie',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('谭杰',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()