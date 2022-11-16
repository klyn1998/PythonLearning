import requests

# requests 模块是第三方的模块，可以用来发送网络连接

response = requests.get('http://localhost:8000')
print(response)  # <Response [200]>

# content 指的是返回的结果，是一个二进制，可以用来传递图片
print(response.content.decode())

# text 获取到的结果就是一个文本
print(response.text)

print(response.status_code)  # 200

# 如果返回的结果是一个json字符串，可以解析json字符串
r = requests.get('http://localhost:8000/test')
print(r.text, type(r.text))  # <class 'str'> 获取到json字符串
print(r.json(), type(r.json()))  # <class 'dict'> 把json字符串解析成为python里对应的数据类型
