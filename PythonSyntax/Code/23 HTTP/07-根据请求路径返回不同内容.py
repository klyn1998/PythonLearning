from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']

    # 状态码：
    # 2XX：OK，请求响应成功
    # 3XX：重定向
    # 4XX：客户端错误  404 客户端访问了一个不存在的地址 405:请求方式不被允许
    # 5XX：服务器错误
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = '欢迎来到test页面'
    elif path == '/demo':
        response = '欢迎来到demo页面'
    else:
        response = '页面走丢了'
        status_code = '404 Not Found'
    start_response(status_code, [('Content-Type', 'text/html;charset=utf8'), ('sss', 'ddd')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app)  # 空为0.0.0.0
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()
