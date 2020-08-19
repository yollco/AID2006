from socket import *


def server():
    tcp_socket = socket()
    tcp_socket.bind(("0.0.0.0", 1516))
    tcp_socket.listen(10)
    connfd, addr = tcp_socket.accept()
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        connfd.send("所以爱会消失对？".encode())
    connfd.close()
    tcp_socket.close()
server()
