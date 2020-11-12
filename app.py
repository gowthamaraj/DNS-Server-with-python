import socket

PORT = 53
IP = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))


def get_flags(data):
    pass


def build_response(data):

    # Transaction ID
    TransactionID = data[0:2]
    TID = ''
    for byte in TransactionID:
        TID += hex(byte)[2:]

    # Get the flags
    Flags = get_flags(data[2:4])


while True:
    data, addr = sock.recvfrom(512)
    r = build_response(data)
    sock.sendto(r, addr)
