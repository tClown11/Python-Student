import time
import threading
import variables

def get_detail_html():
    detail_url_list = variables.detail_url_list
    while True:
        if len(variables.detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url(detail_url_list):
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url, args=variables.detail_url_list)
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html)
        thread_detail_html.start()
    #thread1.setDaemon(True)
    #thread2.setDaemon(True)
    start_time = time.time()


    #thread1.join()
    #thread2.join()
    print("last time: {}".format(time.time() - start_time))