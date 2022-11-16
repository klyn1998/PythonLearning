# 有一个列表name，保存了一组姓名names = ['allen', 'bob', 'jack', 'rose', 'jimmy']
# 再让用户名输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在；
# 如果这个姓名在列表里不存在，就将这个姓名添加到列表里

names = ['allen', 'bob', 'jack', 'rose', 'jimmy']
name = input('请输入姓名')
# if name in names:
#     print('用户姓名已存在')
# else:
#     names.append(name)

for i in names:
    if name == i:
        print('用户姓名已经存在')
        break
else:
    names.append(name)
print(names)

# 冒泡完善
# 统计列表里出现次数最多的元素
# 求列表里的最大数
# 删除列表里的空字符串


