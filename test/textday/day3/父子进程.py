import os
import time

ret = os.fork()#fork命令是linux可用，在window运行会出错

if ret == 0:
    print('-----子进程------')
    time.sleep(1)
else:
    print('-----父进程-----')