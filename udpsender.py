import socket
address = ""
print('UDP sender')
x=socket.socket(type=socket.SOCK_DGRAM)
x.bind(('0.0.0.0',12000))
x.sendto(b'PURPLE EAGLES!',(address,12000))
print('Message sent')
msg, addr=x.recvfrom(2048)
print(msg.decode())
x.close()