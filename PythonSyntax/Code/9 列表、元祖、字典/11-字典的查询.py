person = {'name': 'allen', 'age': 18, 'x': 'y'}

# 查找数据（字典的数据在保存时，是无序的，不能通过下标来获取）
print(person['name'])  # 使用key获取到对应的value
# print(person['height'])  # 如果要查找的key不存在会直接报错

# 需求：获取一个不存在的key时，不报错，而是使用默认值
# 使用字典的get方法，如果key不存在，会默认返回None，而不报错
print(person.get('height'))
# 如果根据key获取不到value，使用给定的默认值
print(person.get('gender', 'female'))  # 不会添加到字典
print(person.get('name', 'bob'))  # allen
print(person)

x = 'age'
print(person[x])
print(person['x'])
# key不可重复，value可重复
