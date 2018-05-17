from socket import *

#创建套接字
serSocket = socket(AF_INET, SOCK_STREAM)

#重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

localAddr = ('', 7788)

serSocket.bind(localAddr)

serSocket.listen(5)

while True:

    print('-----主进程，，等待新客户的到来-----')

    newSocket,destAddr = serSocket.accept()

    print('-----主进程，，接下来负责数据处理[%s]-----'%str(destAddr))

    try:
        while True:
            recvData = newSocket.recv(1024)
            if recvData>0:
                print('recv[%s]:%s'%(str(destAddr), recvData))
            else:
                print('[%s]客户端已断开链接'%str(destAddr))
                break
    finally:
        newSocket.close()
serSocket.close()


'''总结
1.同一时刻只能为一个客户进行服务，不能同时为多个客户端服务
2.类似于找一个‘明星’签字一样，客户端需要耐心等待才可以获取到服务
3.当服务器为一个客户端服务时，而另外的客户端发起了connect，只要服务器listen
的队列有空闲的位置，就会为这个新客户进行连接，并且客户端可以发送数据，但当服务器
为这个新客户端服务时，可能一次性把所有数据接收完毕
'''