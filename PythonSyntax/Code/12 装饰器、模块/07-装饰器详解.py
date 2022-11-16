import time


def cal_time(fn):
    def inner(n, *args, **kwargs):  # 传参数
        start = time.time()
        s = fn(n)
        end = time.time()
        # print('代码耗时', end - start)
        return s, end - start  # return值

    return inner


@cal_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x 


m = demo(10000000, 'good', y='hello')
print(m)
