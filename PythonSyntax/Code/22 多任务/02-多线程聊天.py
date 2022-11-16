import datetime
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('172.22.39.163', 8000))


def send_msg():
    while True:
        msg = input('请输入您要发送的内容')
        if msg == 'exit':
            break
        s.sendto(msg.encode('utf8'), ('172.22.39.163', 9000))


# 接收到的数据是一个元祖
# 元祖里第0个元素是接收到的数据
# 元祖里第1个元素是发送方的ip地址和端口号
def recv_msg():
    while True:
        data, addr = s.recvfrom(1024)
        print(str(datetime.datetime.now()) + '\n接收到了{}地址{}端口的{}'.format(addr[0], addr[1], data.decode('utf8')),
              file=open('chat.txt', 'a'))


t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)
t1.start()
t2.start()
