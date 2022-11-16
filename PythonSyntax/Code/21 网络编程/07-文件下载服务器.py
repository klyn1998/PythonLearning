import socket
import pickle
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.31.199', 9090))
server_socket.listen(128)

# 接收客户端的请求
client_socket, client_addr = server_socket.accept()
file_name = client_socket.recv(1024).decode('utf8')

if os.path.isfile(file_name):
    # print('读取')
    with open(file_name, 'rb') as file:
        content = file.read()
        client_socket.send(content)
else:
    print('文件不存在')
