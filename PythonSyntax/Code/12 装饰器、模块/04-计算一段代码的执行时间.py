import time  # time模块可以获取当前的时间
# 代码运行之前，获取一下时间
start = time.time()  # time模块里的time方法，可以获取当前时间的时间戳
# 时间戳是从 1970-01-01 00:00:00 UTC 到现在的秒数
# UTC +8 计算时-8小时
print('start =', start)
x = 0
for i in range(1, 100000000):
    x += i

print(x)
# 代码运行完成以后，再获取一下时间
end = time.time()

print('代码运行耗时{}秒'.format(end - start))
