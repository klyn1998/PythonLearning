# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]

# 列表的sort方法，会直接对列表进行排序
# nums.sort()
# print(nums)


ints = (5, 9, 8, 7, 2, 3, 1, 6)
# sorted内置函数，不会改变原有的数据，而是生成一个新的有序的列表
x = sorted(ints)
print(x)
print(ints)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'henry', 'age': 20, 'score': 95, 'height': 172}
]


# 字典和字典之间不能使用比较运算
# students.sort()


# foo() takes 0 positional arguments but 1 was given
# foo这个函数需要 0 个位置参数，但是在调用的时候传递了一个参数
def foo(ele):
    print(ele)
    # return ele['age']  # 通过返回值告诉sort方法，按照元素的哪个属性进行排序


# 缺少比较规则，需要传递 key 指定比较规则
# key 参数类型是函数
# 在sort内部实现的时候，调用了foo方法，并且传入了一个参数，参数就是列表里的元素
# students.sort(key=foo)
# print(students)

students.sort(key=lambda ele: ele['age'])
print(students)
