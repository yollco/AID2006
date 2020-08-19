"""
    客户端
"""
from socket import *

udp_client = socket(AF_INET, SOCK_DGRAM)

address = ("127.0.0.1", 1516)
while True:
    msg = input(">>")
    if not msg:
        break
    udp_client.sendto(msg.encode(), address)
    data, addr = udp_client.recvfrom(1024)
    print(data.decode())


udp_client.close()
