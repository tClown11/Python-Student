import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8001))
server.listen()


def handle_sock(sock, addr):
    data = sock.recv(1024)  # data是byte类型
    print(data.decode("utf-8"))
    re_data = input()
    sock.send(re_data.encode("utf-8"))

#获取从客户端发送的数据
#一次获取1k的数据
while True:
    sock, addr = server.accept()

    #用线程去处理新接收的链接（用户）
    cilent_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    cilent_thread.start()
    #data = sock.recv(1024)   #data是byte类型
    #print(data.decode("utf-8"))
    #re_data = input()
    #sock.send(re_data.encode("utf-8"))
    #sock.send("hello {}".format(data.decode("utf-8")).encode("utf-8"))
    #server.close()
    #sock.close()