import socket

# 基于tcp协议的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 在发送数据之前，必须要先和服务器建立连接
s.connect(('172.22.98.21', 9090))
s.send('hello'.encode('utf8'))
s.close()
