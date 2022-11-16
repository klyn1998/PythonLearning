# 列表推导式是使用简单的语法创建一个列表

nums = [i for i in range(10)]
print(nums)

# nums = []
# for i in range(10):
#     nums.append(i)
# print(nums)

x = [i for i in range(10) if i % 2]
print(x)

x = []
for i in range(10):
    if i % 2:  # if后是一个布尔值，0为False，其余为True
        x.append(i)

# points是一个列表，这个列表里的元素都是元祖
points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
print(points)


# 了解即可
# 分组一个list里面的元素，比如[1, 2, 3, ..., 100]变成[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = [i for i in range(1, 101)]
print(m)

n = [m[j:j + 3] for j in range(0, 100, 3)]
print(n)
