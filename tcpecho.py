import socket
x = True
y = socket.socket(type=socket.SOCK_STREAM)
address=('0.0.0.0',14000)
y.bind(address)
y.listen()
while x == True:
        conn, addr=y.accept()
        msg = conn.recv(2048)
        message = msg.decode()
        print(message)
        conn.sendall(b'Hernandez Carlos',14000)
        conn.sendall(b'BYE',14000)
y.close()