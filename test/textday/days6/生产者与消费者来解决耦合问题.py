#encoding=utf-8
import threading
import time
#FIFO（先进先出）——队列
#队列能实现锁原语（可以理解为原子操作，即要么不做，要么就做完）


#python 2 中
#from Queue import Queue

#python 3 中
from queue import Queue
#Queue的说明：
#1.对于Queue，在多线程通信之间扮演重要的角色
#2.添加数据到队列中，使用put()方法
#3.从队列中取数据，使用get()方法
#4.判断队列中是否还有数据，使用qsize()方法

class Producer(threading.Thread):
     def run(self):
         global queue
         count = 0
         while True:
            if queue.qsize() < 1000:
                count = count + 1
                msg = '生产产品'+str(count)
                queue.put(msg)
                print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了' +queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range():
        c = Consumer()
        c.start()
