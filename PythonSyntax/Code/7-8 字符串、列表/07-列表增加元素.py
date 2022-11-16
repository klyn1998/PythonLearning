# 列表是用来保存多个数据的，是有序可变的
# 操作列表，一般都包含增加数据、删除数据、修改数据以及查询数据
# 增删改查

actors = ['jimmy', 'saul', 'mike', 'lydia', 'pinkman', 'white', 'tuco']

# 添加元素的方法 append insert extend
actors.append('howard')
print(actors)  # append在列表最后面追加一个数据

# insert(index, object)  需要两个参数
# index 表示下标，在哪个位置插入数据
# object 表示对象，具体插入哪个数据
actors.insert(1, 'kim')
print(actors)

x = ['nacho', 'victor', 'gus']
# extend(iterable)  需要一个可迭代对象
# A.extend(B) ==> 将可迭代对象 B 添加到 A 里
actors.extend(x)
print(actors)
print(x)



