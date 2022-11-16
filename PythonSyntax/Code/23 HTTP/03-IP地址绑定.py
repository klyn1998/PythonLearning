import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 127.0.0.1 和 0.0.0.0 都表示本机
# 127.0.0.1 只能够通过 127.0.0.1 和 localhost 来访问
# ip地址只能够通过ip地址访问
# 0.0.0.0  表示所有可用的地址

server_socket.bind(('127.0.0.1', 9060))
server_socket.listen(128)
while True:
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024)
    print(data.decode('utf8'))
    client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    client_socket.send('\n'.encode('utf8'))
    client_socket.send('hello'.encode('utf8'))