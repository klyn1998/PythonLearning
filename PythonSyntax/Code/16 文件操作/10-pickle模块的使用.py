# Python里存入数据只支持存入 字符串 和 二进制
# json：将Python里的数据(str/list/tuple/dict/float/bool/None）转换成为对应的json
# pickle：将Python里任意对象转换成为二进制

import pickle

# 序列化  dumps：将Python里的数据转换成为二进制
#        dump：将Python数据转换成为二进制，同时保存到指定文件
# 反序列化 loads：将二进制加载成为Python数据
#         load：读取文件，并加载成为Python里的数据
names = ['allen', 'bob', 'cindy', 'danie']


b_names = pickle.dumps(names)
print(b_names)

file = open('names.txt', 'wb')
file.write(b_names)  # 写入的是二进制，不是纯文本
file.close()
#
file1 = open('names.txt', 'rb')
x = file1.read()
y = pickle.loads(x)
print(y)
file1.close()

# file2 = open('names.txt', 'wb')
# pickle.dump(names, file2)
# file2.close()
#
file3 = open('names.txt', 'rb')
print(pickle.load(file3))

# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def eat(self):
#         print(self.name + 'is eating shit')
#
#
# d = Dog('黑皮狗', 'black')
# # 保存到文件里
# pickle.dump(d, open('dog.txt', 'wb'))
#
# # 文件里加载出来
# dd = pickle.load(open('dog.txt', 'rb'))
# print(dd.name, dd.color)
# dd.eat()

# pickle 和 json 的区别，什么情况用json，什么情况用pickle

# pickle 用来将数据原封不动地转换成为二进制。
# 但是这个二进制，只能在Python里识别。

# json只能保存一部分信息，作用是用来在不同的平台里传递数据
# json里存储的数据都是基本数据类型
