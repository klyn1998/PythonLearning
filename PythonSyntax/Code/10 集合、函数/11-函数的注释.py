def add(a: int, b: int):  # 仍然可以使用 'str'，限制不严格
    """
    这个函数用来将两个数字相加
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字相加的结果
    """
    return a + b


x = add(1, 2)
print(x)
y = add('hello', 'world')
print(y)
# z = add('hello', 5)  # 报错
# print(z)

# help(add)
