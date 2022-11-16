# 生成器的形式就相当于一个函数

def my_gen(n):
    i = 0
    while i < n:
        yield i  # 使用 yield 结果是一个生成器
        i += 1
        # return i  # return 表示一个函数的结束


m = my_gen(10)  # 获取一个生成器，不会调用my_gen这个函数
for a in m:
    print(a)
# print(next(m))  # 当调用next方法，获取数据时，才会调用方法
# print(next(m))  # 再执行next方法，会从上一次yield出来的位置继续执行代码
# print(next(m))


def fibonacci(n):
    i = 0
    num1 = num2 = 1
    while i < n:
        i += 1
        yield num1
        num1, num2 = num2, num1 + num2


f = fibonacci(9)
# for x in f:
#     print(x)
