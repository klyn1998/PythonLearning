def calc(a, b, fn):
    return fn(a, b)


# def add(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b


# 回调函数
# x1 = calc(1, 2, minus)
# x2 = calc(2, 5, add)
# print(x1, x2)

x3 = calc(1, 2, lambda a, b: a + b)
x4 = calc(2, 7, lambda a, b: a - b)
x5 = calc(3, 9, lambda p, q: p * q)
print(x4)
