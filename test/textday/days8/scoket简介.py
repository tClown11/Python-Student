#创建socket
scoket.socket(AddressFamily, Type)
#AddressFamily:可以选择AF_INET（用于Internet进程间通信）或者AF_UNIX（用于同一台机器进程间通信），实际工作中常用AF_IENT
#Type：套接字类型，可以是SOCK_STREAM（流式套接字，主要用于TCP协议）或者SOCK_DGRAM（数据报套接字，主要用于UDP协议）


#创建一个tcp socket：
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket Created')

#创建一个udp socket:
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Created')