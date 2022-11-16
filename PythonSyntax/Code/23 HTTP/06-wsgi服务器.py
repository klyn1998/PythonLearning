from wsgiref.simple_server import make_server


# demo_app 需要两个参数
# 第 0 个参数表示环境（电脑的环境；请求路径相关的环境）
# 第 1 个参数是一个函数，用来返回响应头
# 这个函数需要一个返回值，返回值是一个列表
# 列表里只有一个元素，是一个二进制，表示返回给浏览器的内容
def demo_app(environ, start_response):
    # environ是一个字典，保存了很多的数据
    # 其中有PATH_INFO，能够获取到用户的访问路径
    path = environ['PATH_INFO']
    print('path={}'.format(path))
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ('sss', 'ddd')])
    return ['你好'.encode('utf8')]


if __name__ == '__main__':
    # demo_app是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()
