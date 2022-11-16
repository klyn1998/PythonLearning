person = {'name': 'allen', 'age': 18, 'height': '180cm'}

# 列表和元祖里是一个单一数据，但是字典是键值对的形式

# 第一种遍历方式：直接for...in循环字典
for key in person:  # for...in循环获取到的是key
    print(key, '=', person[key])

# 第二种方式：获取到所有的key，然后再遍历key，根据key获取value
# print(person.keys())  # dict_keys(['name', 'age', 'height'])
for k in person.keys():
    print(k, '=', person[k])

# 第三种方式：获取到所有的value
# 只能拿到值，不能拿到key
print(person.values())  # 列表
for v in person.values():
    print(v)

# 第四种遍历方式：
# print(person.items())  # dict_item([('name', 'allen'), ('age', 18), ('height', '180cm')])

for item in person.items():  # 列表里的元素是元祖，把元祖当作整体进行遍历
    print(item[0], '=', item[1])

for a, b in person.items():  # 拆包
    print(a, '=', b)
# 一般使用方法一、四
