#coding=utf-8
from socket import *

#1.创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2.准备接收方地址
sendAddr = ('192.168.1.103', 8080)

#3.从键盘获取数据
sendData = raw_input("请输入要发送的数据：")

#4.发送数据到指定电脑上
udpSocket.sendto(sendData, sendAddr)

#5.等待接收对方发送的数据
recvData = udpSocket.recvfrom(1024)#1024表示本次接收的最大字节数

#6.显示对方发送的数据
print(recvData)

#7.关闭套接字
udpSocket.close()