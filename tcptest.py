import socket
y = socket.socket(type=socket.SOCK_STREAM)
address=('35.231.78.56',14000)
y.connect(address)
y.sendall(b'Connection Stablished',14000)
msg = y.recv(2048)
message = msg.decode()
print(message)
y.close()