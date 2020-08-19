"""
    服务端
"""
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(("0.0.0.0", 1516))
while True:
    print("---------------------")
    data, addr = udp_socket.recvfrom(1024)
    print("地址和端口是", addr)
    udp_socket.sendto("所以爱会消失对？".encode(), addr)
    print("发送成功")

udp_socket.close()
