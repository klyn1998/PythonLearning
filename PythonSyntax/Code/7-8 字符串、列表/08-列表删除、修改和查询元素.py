mexicans = ['nacho', 'victor', 'jack', 'gus', 'tuco']

# 删除数据有三个相关的方法 pop remove clear

# pop 默认会删除列表里最后一个数据，并且返回这个数据
# pop 还可以传入index参数，用来删除指定位置上的数据
x = mexicans.pop(3)
print(x)  # tuco
print(mexicans)

#  remove 用来删除指定的元素
mexicans.remove('nacho')
# mexicans.remove('mike')  # 数据在列表中不存在，会报错
print(mexicans)

# # clear 用来清空一个列表
# mexicans.clear()
# print(mexicans)  # []

# 使用del 也可以删除一个数据
del mexicans[1]
print(mexicans)

# a = 100
# del a
# print(a)  # 报错

americans = ['jimmy', 'saul', 'kim', 'mike', 'white', 'kim']
# 查询相关的方法  index count
print(americans.index('kim'))  # 2
# print(americans.index('tim'))  # 如果元素不存在，报错
print(americans.count('kim'))
# in 运算符
print('saul' in americans)  # True
print('tim' in americans)  # False

# 修改元素
# 使用下标可以直接修改列表里的元素
americans[5] = 'lydia'
print(americans)
