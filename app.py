import socket

PORT = 53
IP = "127.0.0.1"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

while True:
    data, addr = sock.recvfrom(512)

