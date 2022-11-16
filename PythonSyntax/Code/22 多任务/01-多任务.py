import threading
import time


def eat():
    for i in range(50):
        time.sleep(0.2)
        print('eat')


def drink():
    for i in range(50):
        time.sleep(0.2)
        print('drink')


# 多个任务同时执行
# Python里执行多任务：多线程、多进程、多进程+多线程
# eat()
# drink()

# target 需要的是一个函数，用来指定线程需要执行的任务
t1 = threading.Thread(target=eat)  # 创建了线程1
t2 = threading.Thread(target=drink)  # 创建了线程2

# 启动线程
t1.start()
t2.start()
