import json
from wsgiref.simple_server import make_server


def read_file(file_name, **kwargs):
    try:
        with open(file_name) as file:
            content = file.read()
            if kwargs:
                content = content.format(**kwargs)
            return content
    except FileNotFoundError:
        print('文件不存在')


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'allen', 'age': 18})
    elif path == '/demo':
        response = read_file('note.txt')
    elif path == '/hello':
        response = read_file('hello.html')
    elif path == '/info':
        response = read_file('info.html', username='allen')
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
