# split rsplit splitlines partition

# 字符串类型的数据
x = 'jerry-henry-merry-jack-tony'
# ['jerry', 'henry', 'merry', 'jack', 'tony']
# 使用split方法，可以将一个字符串切割成一个列表
y = x.split('-')
print(x)
print(y)  # 切割以后的结果是一个列表

m = x.split('-', 2)  # 分割两次 ['jerry', 'henry', 'merry-jack-tony']
print(m)

z = x.rsplit('-', 2)  # 从右边分割，数据还是正的
print(z)

a = 'hello\nworld\nnihao'
print(a.splitlines())  # ['hello', 'world'] 换行分割

# partition 指定一个字符串作为分割符，分为三部分
# 前面 分割符 后面
print('abcdefXopqrst'.partition('X'))  # ('abcdef', 'X', 'opqrst')
print('abcdefXmpXqrst'.rpartition('X'))  # ('abcdefXmp', 'X', 'qrst')

# 获取文件名和后缀名
print('不要打开.mp4'.rpartition('.'))
