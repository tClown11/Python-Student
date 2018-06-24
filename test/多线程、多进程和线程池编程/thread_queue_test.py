import time
import threading
from queue import Queue


def get_detail_html(queue):
    while True:

        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=detail_url_queue)
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=detail_url_queue)
        thread_detail_html.start()
    #thread1.setDaemon(True)
    #thread2.setDaemon(True)
    start_time = time.time()
    detail_url_queue.task_done()
    detail_url_queue.join()

    #thread1.join()
    #thread2.join()
    print("last time: {}".format(time.time() - start_time))