from socket import *
import pickle
import os

host = ""
port = 13000
buf = 1024
address = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(address)


while True:
    (data, address) = UDPSock.recvfrom(buf)
    print("Received message: " + pickle.loads(data))
    if data == "exit":
        UDPSock.close()
        break

os._exit(0)
