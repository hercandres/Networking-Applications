import socket
address = ""
x=socket.socket(type=socket.SOCK_DGRAM)
x.bind(('0.0.0.0',12000))
msg,addr=x.recvfrom(2048)
print(msg.decode())
x.sendto(b'Message Received by listener',(address,12000))
print('echo sent')
x.close()