def test1():
    print('test1 starts')
    print('test1 ends')


def test2():
    print('test2 starts')
    test1()
    print('test2 ends')


test2()


# 定义求[n, m)之间所有整数之和
def add(n, m):
    x = 0
    for i in range(n, m):
        x += i
    return x


result = add(0, 101)
print(result)


# 求n的阶乘
def fac(n):
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m


# 计算m阶乘的和
def add1(p):
    q = 0
    for i in range(1, p + 1):
        q += fac(i)
    return q


print(add1(5))
