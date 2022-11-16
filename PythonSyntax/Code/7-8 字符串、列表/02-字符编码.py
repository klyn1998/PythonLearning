# ASCII --> Latin1 --> Unicode编码
# 字符 --> 数字编码存在一个对应的关系

# 使用内置函数 chr 和 ord 能够查看数字和字符的对应关系
# ord 获取字符对应的编码；chr 根据编码获取对应的字符
print(ord('a'))  # 字符对应的编码是97

print(chr(65))

print(ord('你'))
print(chr(20320))

# GBK utf-8 BIG5
# GBK：国标扩，汉字占两个字节，简体中文
# BIG5：繁体中文
# utf-8：统一编码，汉字占三个字节

# 使用字符串的encode编码，可以将字符串转换成为指定编码集结果
# 如果有一个编码集的结果，想把它转换成为对应的字符，使用decode

# GBK 一个汉字两个字节
print('你'.encode('gbk'))  # b'\xc4\xe3'

# utf8 一个汉字三个字节
print('你'.encode('utf8'))  # b'\xe4\xbd\xa0'

x = b'\xe4\xbd\xa0'
print(x.decode('utf8'))

# 把'你好'使用 gbk 编码
y = '你好'.encode('utf8')  # utf8 一个汉字转换成三个字节
print(y)  # b'\xe4\xbd\xa0  \xe5\xa5\xbd'

# gbk 一个汉字占两个字节
print(y.decode('gbk'))  # 浣犲ソ  \xe4\xbd  \xa0\xe5  \xa5\xbd
print(y.decode('utf8'))

# txt 文本乱码，修改字符集
