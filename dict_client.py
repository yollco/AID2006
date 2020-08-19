import socket

# 测试地址与接口
addrsse = ("127.0.0.1", 1516)
# 套接字
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    english = input(">>")
    if not english:
        print("程序结束啦！")
        break
    # 发送单词
    udp_client.sendto(english.encode(), addrsse)
    # 接收单词意思
    data, addr = udp_client.recvfrom(1024)
    # 判断data为空则继续输入查找
    if not data:
        print("没有这个单词哦！请继续查找-------------------")
    # 打印单词意思
    print("单词意思是：", data.decode())

udp_client.close()
