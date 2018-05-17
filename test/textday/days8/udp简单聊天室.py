#coding=utf-8

from socket import *
from time import ctime

#1.创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2.绑定本地的相关信息
bindAddr = ('', 7788)#ip地址和端口号，ip地址一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr)

while True:

    #3.等待对方发送的数据
    recvData = udpSocket.recvfrom(1024)#1024表示本次接收的最大字节数

    #4.打印信息
    print('【%s】%s:%s'%(ctime(), recvData[1][0], recvData[0]))

#5.关闭套接字
udpSocket.close()