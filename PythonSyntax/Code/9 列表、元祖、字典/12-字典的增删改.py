person = {'name': 'allen', 'age': 18, 'addr': 'Japan'}

# 直接使用key可以修改对应值的value
print(person['name'])
person['name'] = 'bob'
print(person['name'])

# 如果key存在，修改key对应的value
# 如果key不存在，会往字典里添加一个新的key-value
person['gender'] = 'female'
print(person)

# 把name对应的键值对删除了，执行结果是被删除的value
x = person.pop('name')
print(person)
print(x)  # bob

# popitem 删除一个元素，结果是被删除的这个元素组成的键值对
x = person.popitem()
print(x)  # ('gender', 'female')
print(person)

del person['addr']
print(person)

person.clear()  # 清空一个字典
print(person)  # {}
