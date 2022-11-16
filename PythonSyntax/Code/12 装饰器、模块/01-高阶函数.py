# 1. 把一个函数当做另一个函数的返回值
def test():
    print('我是test函数')
    return 'hello'


def demo():
    print('我是demo函数')
    return test


def bar():
    print('我是bar函数')
    return test()


# x = test()
# print(x)

# y = demo()  # 起别名
# print(y)  # <function test at 0x7faaa98d3040> 函数的类型和内存地址
# z = y()
# print(z)  # hello

a = bar()  # 执行bar，并把bar的结果赋值给a
# # b = bar  # 起别名
print(a)

# 2. 把一个函数当作另一个函数的参数 lambda表达式的使用
# sort filter map reduce

# 3. 在函数内部再定义一个函数
