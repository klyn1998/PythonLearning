# 元祖和列表很像，都是用来保存多个数据
# 使用一对小括号() 来表示一个元祖
# 元祖和列表的区别在于，列表是可变的，而元祖是不可变数据类型
words = ['hello', 'yes', 'good', 'hi']  # 列表，使用[]表示
nums = (9, 4, 3, 1, 6, 7, 9, 3, 9)  # 元祖，使用()表示

# 和列表一样，也是一个有序的存储数据的容器
# 可以通过下标来获取元素
print(nums[3])
# nums[3] = 40  # 报错；不可变数据类型，无法修改
print(nums.index(9))
print(nums.count(9))

# 特殊情况：如何表示只有一个元素的元祖？
ages = (18,)  # 如果元祖里只有一个元素，要在最后面加','
print(type(ages))  # <class 'tuple'>

# tuple 内置类
print(tuple('apple'))

# 怎么样把列表转换成为元祖？元祖转换成为列表
print(tuple(words))  # tuple list set 都是这样使用的
print(list(nums))

height = ('189', '170', '160')
print('*'.join(height))
print(''.join(('h', 'e', 'l', 'l', 'o')))

# 元祖也可以遍历
for i in nums:
    print(i)
