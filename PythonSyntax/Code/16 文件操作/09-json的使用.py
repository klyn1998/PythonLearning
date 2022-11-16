import json

# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write时，只能写入字符串或二进制
# 字典、列表、数字等都不能直接写入到文件里

# 将数据转换成为字符串：repr/str 更多使用json模块
# json 本质就是字符串，区别在于json里要使用双引号表示字符串
# 将数据转换成为二进制：使用pickle模块

names = ['allen', 'bob', 'cindy', 'danie']
# x = json.dumps(names)
# print(x, type(x))
file = open('names.txt', 'w')
# file.write(x)


# json 里将数据持久化有两个方法
# dumps：将数据转换成为json字符串，不会将数据保存到文件里
# dump：将数据转换成为json字符串，同时写入到指定文件
# json.dump(names, open('dump.txt', 'w'))
# file.close()

# json 反序列化也有两个方法
# loads：将json字符串加载成为Python里的数据
# load：读取文件，把读取的内容加载成为Python里的数据
x = '{"name": "allen", "age": 18}'  # 符合json规则的字符串
p = json.loads(x)
print(p, type(p))
print(p['name'])

# load 读取一个文件，并把文件里的json字符串加载成为一个对象
y = json.load(open('dump.txt'))
print(y[1])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + 'is eating')


p = Person('allen', 18)
x = json.dumps(p.__dict__)
print(x)
y = json.loads(x)
print(y, type(y))  # <class 'dict'>
