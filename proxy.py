import socket

print('python proxy server started')
#create a tcp socket

my_sock = socket.socket()
my_sock.bind(('0.0.0.0',14000))

print('Bind called for port 14000')

#makesure apach 2 is turned off = sudo systemctl stop>

my_sock.listen(8)
print('listening')

client_conn, client_addr = my_sock.accept()
print('Client accepted')

data = client_conn.recv(2048)
print('Data Collected')
message = data.decode()
print('Data decoded')
print(message)



token_list = data.decode().split()
print(token_list)
cmd = token_list[0]
print(cmd)

if cmd == 'GET':
  target = token_list[1][1:]
  print(target)
  
  # try to get a webpage from target_url and
  # send back to our client

  # send a request to target_url

  s = socket.socket()
  # replace niagaracomputing.org with the external IP>
  # target = 'niagaracomputing.org'
  s.connect((target, 80)) # recall 80 is the required>

  # replace niagaracomputing.org with the external IP>

  s.sendall('GET / HTTP/1.0\r\n'.encode())

  #s.sendall('Host: computeraugmented.com\r\n'.encode>
  # example target = 'computeraugmented.com'
  #s.sendall('Host: target\r\n'.encode()) # DOP! we d>
  x = 'Host: ' + target + '\r\n\r\n'
  s.sendall(x.encode())

  resp = s.recv(2048)

else:
  print('unrecognized command')

#send html of target file back to client
print('RESPONSE:', resp)

client_conn.sendall(resp)

print('Information sent')


client_conn.close()
print('Incoming connection closed')
my_sock.close()
print('python server complete')