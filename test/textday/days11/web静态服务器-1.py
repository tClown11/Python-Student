#coding=utf-8
import socket

from multiprocessing import Process

def headleClient(client_socket):
    """用一个新的进程，为一个客户端进行服务"""
    client_data = client_socket.recv(1024)
    requestHeaderLines = client_data.splitlines()
    for line in requestHeaderLines:
        print(line)

    responseHeaderLines = "HTTP/1.1 200 OK\r\n"
    responseHeaderLines += "\r\n"
    responseBody = "hello world"

    response = requestHeaderLines + responseBody
    client_socket.send(response)
    client_socket.close()

def main():
    #创建Socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8000))
    server_socket.listen(128)

    #监听并创建进程
    while True:
        client_socket, client_addr = server_socket.accept()
        clientP = Process(target=headleClient, args=client_socket)
        clientP.start()
        server_socket.close()






if __name__ == "__main__":
    main()