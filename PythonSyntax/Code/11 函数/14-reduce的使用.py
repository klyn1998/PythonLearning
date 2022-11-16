# 导入模块的语法
from functools import reduce


# reduce 之前是一个内置函数
# 内置函数和内置类都在builtin.py文件里
def foo(x, y):
    return x + y


scores = [100, 89, 76, 87]

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]


# def bar(x, y):
#     if type(x) == dict and type(y) == dict:
#         return x['age'] + y['age']
#     elif type(x) == int and type(y) == dict:
#         return x + y['age']


# def bar(x, y):
#     return x + y['age']


print(reduce(lambda x, y: x + y['age'], students, 0))  # initial 指定初始化的值
