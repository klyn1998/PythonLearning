# +：可以用来拼接，用于 字符串、元祖、列表
print('hello' + 'world')
print(('good', 'yes') + ('hi', 'ok'))
print([1, 2, 3] + [4, 5, 6])

# -：只能用于集合，求差集
print({1, 2, 3} - {3})

# *：可以用于字符串、元祖、列表，表示重复多次。不能用于字典和集合：不能重复
print('hello' * 3)
print([1, 2, 3] * 3)
print((1, 2, 3) * 3)

# in：成员运算符
print('a' in 'abc')
print(1 in [1, 2, 3])
print(1 in (1, 2, 3))
# in 用于字典判断key是否存在
print('age' in {'name': 'allen', 'age': 18})
print(1 in {1, 2, 3})

# 带下标的遍历 enumerate 类的使用，一般用于列表和元祖等有序的数据
# nums = (19, 82, 39, 12, 34, 58)
# nums = [19, 82, 39, 12, 34, 58]
nums = {19, 82, 39, 12, 34, 58}
for i, e in enumerate(nums):
    print('第%d个数据是%d' % (i, e))

person = {'name': 'allen', 'age': 18}
for i, e in enumerate(person):
    print(i, e)
