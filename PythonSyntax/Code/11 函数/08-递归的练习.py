# 使用递归求n!
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(4))


# 使用递归求斐波那契数列第n个数字
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(9))
