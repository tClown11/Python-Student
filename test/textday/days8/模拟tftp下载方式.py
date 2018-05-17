import socket
f = open("test.jpg", "bw")
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind()

while True:
    recvData = udpScoket.recvfrom(1024)
    if xxx:
        #没有数据了
        break
    else:
        #收到数据
        f.write(recvData)

f.close()