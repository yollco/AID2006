from socket import *
def client():
    address = ("127.0.0.1", 1516)
    tcp_client = socket()
    tcp_client.connect(address)
    while True:
        msg = input(">>")
        if not msg:
            break
        tcp_client.send(msg.encode())
        data = tcp_client.recv(1024)
        print(data.decode())
    tcp_client.close()
client()
