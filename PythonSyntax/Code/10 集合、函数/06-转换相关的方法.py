import json

# 内置类 list tuple set
nums = [9, 8, 4, 3, 2, 1]
x = tuple(nums)  # 使用tuple内置类转换为元祖
print(x)

y = set(x)  # 使用set内置类转换为集合

z = list({'name:': 'zhangsan', 'age': 18, 'score': 98})
print(z)  # ['name:', 'age', 'score'] 都为key

# Python里有一个比较强大的内置函数，可以执行字符串里的代码
a = 'input("请输入用户名")'  # a是一个字符串
b = '1 + 1'
# eval(a)
print(eval(b))

# JSON的使用，把列表、元祖、字典等转换成为JSON字符串

person = {'name': 'allen', 'age': 18, 'gender': 'female'}
m = json.dumps(person)  # dumps将字典、列表、集合、元祖等转换成为JSON字符串
print(m)  # '{"name": "allen", "age": 18, "gender": "female"}'
print(type(m))  # <class 'str'>

# Python            JSON
# True              true
# False             false
# 字符串             字符串
# 字典               对象
# 列表、元祖          数组
print(json.dumps(['hello', 'good', 'yes', True]))
print(json.dumps(('hello', 'good', 'yes', False)))

# n = '{"name": "allen", "age": 18, "gender": "female"}'
n = '["hello", "good"]'  # 数组转为列表
p = eval(n)
print(p, type(p))
s = json.loads(n)  # loads可以将json字符串转化成为Python里的数据
print(s, type(s))
