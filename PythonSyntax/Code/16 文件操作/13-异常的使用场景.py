age = input('请输入年龄：')  # input 接收到的用户输入是一个字符串

try:
    age = float(age)
except ValueError:
    print('请输入数字')
else:
    if age > 18:
        print('welcome')
    else:
        print('leave please')

# 或采用正则表达式判断

