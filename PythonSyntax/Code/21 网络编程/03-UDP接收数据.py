import socket

# 创建一个基于 udp 的网络socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口号和ip地址
s.bind(('192.168.31.199', 9090))

# recvfrom 接收数据
content = s.recvfrom(1024)  # recvfrom是一个阻塞的方法，一直等待
# print(content)
# (b'\xe4\xb8\x8b\xe5\x8d\x88\xe5\xa5\xbd', ('192.168.31.185', 60737))
# 接收到的数据是一个元祖，元祖里有两个元素
# 第0个是接收到的数据，第1个元素是发送方的ip地址和端口号
print('从{}地址{}端口号接收到了{}'.format(content[1][0], content[1][1], content[0].decode('utf8')))

s.close()
