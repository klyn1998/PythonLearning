try:
    file = open('01-exercise.py', 'r')
except FileNotFoundError:
    print('文件未找到')
else:
    try:
        file.read()
    finally:
        file.close()

try:
    with open('01-exercise.py', 'r') as file:
        file.read()  # 不需要再手动关闭文件
except FileNotFoundError:
    print('文件未找到')

x = open('01-exercise.py')
print(type(x))  # <class '_io.TextIOWrapper'>

# with我们称之为上下文管理器，很多需要手动关闭的连接
# 比如说 文件连接，socket连接，数据库的连接 都能使用with关键字自动关闭连接
# with 关键字后面对象，需要实现 __enter__ 和 __exit__ 魔法方法
