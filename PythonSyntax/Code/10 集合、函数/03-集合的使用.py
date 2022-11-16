# 集合是一个不重复的无序数据集，可以使用 {} 或者 set 来表示
# {} 有两种意思：字典、集合
# {} 里如果放的是键值对，它就是一个字典；如果放的是单个的值，就是一个集合
person = {'name': 'zhangsan', 'age': 18}  # 字典
x = {'hello', 1, 'good'}

# 如果有重复的数据，会自动去除
names = {'zhangsan', 'lisi', 'jack', 'tony', 'jack', 'lisi'}
print(names)  # {'zhangsan', 'lisi', 'jack', 'tony'}

# set 增删
names.add('allen')  # 添加一个元素
print(names)

names.pop()  # 删除一个
print(names)

# names.remove('jack')   # 删除一个指定的元素；元素不存在则报错
print(names)

# union 将多个集合合并生成一个新的集合
# A.update(B) 将B拼接到A里
print(names.union({'tim', 'kim'}))
print(names)

names.update(['apple', 'iphone'])
print(names)

names.clear()  # 清空一个集合
# 空集合的表示方式不是{}；{}表示的是空字典；
# 空集合 set()
print(names)

print('jack' in names)  # False
