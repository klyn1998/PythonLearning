# mode 指的是文件的打开方式
# r: read 只读模式，默认，打开文件之后，只能读取，不能写入
# 如果文件不存在，会报错
# file = open('xxx.txt', 'r')
# print(file.read())
# file.write('hello')  # 不能执行写入操作，会报错
# file = open('xxs.txt', 'r')  # 文件不存在，会报错

# w: write 写入模式，打开文件之后，只能写入，不能读取
# 如果文件存在，会覆盖文件；如果文件不存在，会创建文件
# file = open('xxx.txt', 'w')
# file.read()  # 不能执行读取，会报错
# file = open('yyy.txt', 'w')
# file.write('你好')

# b: 以二进制的形式打开文件，可以用来操作非文本文件
# rb：以二进制读取  wb：以二进制写入
# file = open('xxx.txt', 'rb')
# print(file.read())  # 读取的结果是二进制
# file = open('xxx.txt', 'wb')
# file.write('大家好')  # 报错，只能写入二进制
# file.write('大家好'.encode('utf8'))

# a：追加模式，会在最后追加内容。
# 如果文件不存在，会创建文件；如果文件存在，会追加

# r+：可读写 一般不用
# w+：可读写 一般不用
file = open('yyy.txt', 'w+')
print(file)
file.write('哈哈哈')
file.seek(0, 0)  # 写入之后，文件指针到最后了，需要调用seek将文件指针重置到开头
print(file.read())

file.close()
