# Python里使用 open 内置函数用来打开一个文件
# file：文件的路径。相对路径和绝对文件
# mode：打开文件的模式 r：只读 w：写入 b：二进制 t：文本形式打开
# mode默认使用rt
# encoding：用来指定文件的编码方式，mac里默认utf8
# file = open('xxx.txt')  # 报错，默认是以rt打开，文件不存在会报错
# file = open('sss.txt', 'w', encoding='utf8')  # 创建一个新的文件
# file.write('你好')
# file.close()

file = open('sss.txt', 'r')
# print(file.read())  # 将所有的数据都读取出来
# print(file.readline())  # 只读取一行数据

# while True:
#     content = file.readline()
#     print(content)
#     if content == '':
#         break

# 读取所有行的数据，保存到一个列表里
print(file.readlines())

x = file.read(12)  # 指的是读取的长度
print(x)

# 优化：没有绝对的优化，除非提升硬件
# 软件层面：时间 / 空间
# 大文件，每次只读1024
while True:
    content = file.read(1024)  # 每次读1024字节，光标后移
    if not content:
        break
    print(content)


file.close()
