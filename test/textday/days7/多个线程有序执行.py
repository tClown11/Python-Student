from threading import Thread,Lock
from time import sleep
#总结：可以使用互斥锁完成多个任务，有序的进程工作，这就是线程的同步


#创建三个线程的类，并使其相互解锁，完成有序执行的任务
class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("------Task 1------")
                sleep(0.5)
                lock2.release()

class Task2(Thread):
    def run(self):
        while Ture:
            if lock2.acquire():
                print("------Task 2------")
                sleep(0.5)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("------Task 3------")
                sleep(0.5)
                lock1.release()

#使用lock创建出的锁默认没有“上锁”
lock1 = Lock()
#创建另外两把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()
lock3 = Lock()
lock3.acquire()

#实例化对象,创建三个线程
t1 = Task1()
t2 = Task2()
t3 = Task3()

#开启线程
t1.start()
t2.start()
t3.start()