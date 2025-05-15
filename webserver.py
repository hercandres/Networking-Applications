import socket

print('python http server started')
#create a tcp socket

my_sock = socket.socket()
my_sock.bind(('0.0.0.0',80))

print('Bind called for port 80')

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
  target_file = token_list[1][1:]
  print(target_file)
  f = open(target_file, 'r')
  file_contents = f.read()
  print(file_contents)
  resp = 'HTTP/1.1 200 OK\r\n'
  resp += 'Content-Type: text/html \r\n\r\n'
  resp += file_contents
else:
  print('unrecognized command')



resp = resp.encode()
print('RESPONSE:', resp)
client_conn.sendall(resp)

print('Information sent')


client_conn.close()
print('Incoming connection closed')
my_sock.close()
print('python server complete')