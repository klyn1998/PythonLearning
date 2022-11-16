import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))
server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')

    path = data.splitlines()[0].split(' ')[1]
    print('请求的路径是%s' % path)
    response_body = 'hello world'
    response_header = 'HTTP/1.1 200 OK\n'  # 200 OK 成功了

    if path == '/login':
        response_body = '欢迎登陆'
    elif path == '/register':
        response_body = '欢迎注册'
    elif path == '/':
        response = '欢迎来到首页'
    else:
        # 页面未找到 404 Page Not Found
        response_header = 'HTTP/1.1 404 Page Not Found\n'
        response_body = '页面不存在'

    response_header += '\n'
    response = response_header + response_body
    client_socket.send(response.encode('gbk'))
