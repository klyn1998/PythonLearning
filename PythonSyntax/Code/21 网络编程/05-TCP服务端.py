import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('172.22.98.21', 9090))

# 1000  1120 ==> 120 排队
# 1000  1130 ==> 128 排队  2 失败
s.listen(128)  # 把socket变成一个被动监听的socket

# (
# <socket.socket fd=512, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.31.199', 9090), raddr=('192.168.31.185', 38096)>,
# ('192.168.31.185', 38096)
# )
# 接收到的数据是一个元祖，元祖里有两个元素
# 第0个元素是客户端的socket连接，第1个元素是客户端的 ip 地址和端口号
client_socket, client_addr = s.accept()  # 接收客户端的请求

# udp里接收数据，使用recvfrom
text = client_socket.recv(1024)  # tcp里使用recv获取数据
print('接收到了{}客户端{}端口号的{}'.format(client_addr[0], client_addr[1], text))

s.close()
