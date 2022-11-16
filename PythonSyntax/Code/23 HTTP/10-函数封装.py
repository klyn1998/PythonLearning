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


def index():
    return '欢迎来到我的首页'


def show_test():
    return json.dumps({'name': 'allen', 'age': 18})


def show_demo():
    return read_file('note.txt')


def show_hello():
    return read_file('hello.html')


def show_info():
    return read_file('info.html', username='allen')


url = {'/': index,
       '/test': show_test,
       '/demo': show_demo,
       '/hello': show_hello,
       'info': show_info
       }


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    method = url.get(path)
    if method:
        status_code = '200 OK'
        response = method()
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
