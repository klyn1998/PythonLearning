def add(a, b):
    return a + b


def add_many(iterable):
    x = 0
    for n in iterable:
        x += n
    return x


nums = [1, 2, 3, 4, 5, 8, 10, 12]
print(add_many(nums))

# 一次input只能接受一次用户的输入
nums = []
while True:
    num = input('请输入数字，输入exit退出')
    if num == 'exit':
        break
    nums.append(int(num))
print(nums)
