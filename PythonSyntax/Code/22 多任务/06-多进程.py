import multiprocessing
import time
import os


def eat(n):
    for i in range(n):
        time.sleep(0.5)
        print('eating, pid={}'.format(os.getpid()))


def drink(n):
    for i in range(n):
        time.sleep(0.5)
        print('drinking, pid={}'.format(os.getpid()))


if __name__ == '__main__':
    print('主进程的pid={}'.format(os.getpid()))
    # 创建了两个进程
    # target 用来表示执行的任务
    # args 用来传参，类型是一个元祖
    p1 = multiprocessing.Process(target=eat, args=(100,))
    p2 = multiprocessing.Process(target=drink, args=(100,))

    p1.start()
    p2.start()
