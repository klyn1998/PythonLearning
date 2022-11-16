import socket

# HTTP服务器都是基于TCP的socket连接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))
server_socket.listen(128)

# 获取到的数据是一个元祖，元祖里有两个元素
# 第0个元素是客户端的socket连接，第一个元素是客户端的ip地址和端口号
client_socket, client_addr = server_socket.accept()

# 从客户端的socket里获取数据
data = client_socket.recv(1024)
print(data.decode('utf8'))  # 请求头

# 返回内容之前，需要先设置HTTP响应头
# 设置一个响应头就空一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))

# 所有的响应头设置完成后，再换行
client_socket.send('\n'.encode('utf8'))

# 发送内容
client_socket.send('hello'.encode('utf8'))
