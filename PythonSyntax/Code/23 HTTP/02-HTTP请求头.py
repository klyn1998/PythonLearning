import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))
server_socket.listen(128)
client_socket, client_addr = server_socket.accept()
data = client_socket.recv(1024)
print(data.decode('utf8'))
"""
GET / HTTP/1.1  
# GET 请求方式，GET/POST/PUT/DELETE......
# / 请求的路径 (index.html) 以及请求参数
# HTTP/1.1 HTTP版本号

Host: 172.22.76.75:9090  # 请求的服务器地址
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1

# UA 用户代理，最开始设计的目的是为了能从请求头里辨识浏览器的类型
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
"""
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
client_socket.send('\n'.encode('utf8'))
client_socket.send('hello'.encode('utf8'))
