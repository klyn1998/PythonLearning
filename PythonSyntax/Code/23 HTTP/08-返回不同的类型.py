import json
from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    # print(environ.get('QUERY_STRING'))  # 获取到客户端GET请求方式传递的参数
    # 还有POST请求数据

    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'allen', 'age': 18})
    elif path == '/demo':
        with open('note.txt', 'r') as file:
            response = file.read()
    elif path == '/hello':
        with open('hello.html', 'r') as file:
            response = file.read()
    elif path == '/info':
        name = 'jack'
        with open('info.html', 'r') as file:
            response = file.read().format(username=name)
    else:
        response = '页面走丢了'
        status_code = '404 Not Found'
    start_response(status_code, [('Content-Type', 'text/html;charset=utf8'), ('sss', 'ddd')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()
