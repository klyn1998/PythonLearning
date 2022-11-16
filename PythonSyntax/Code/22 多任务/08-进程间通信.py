import multiprocessing
import os
import time


def produce(x):
    for i in range(10):
        time.sleep(0.5)
        print('生产了pid{} {}'.format(os.getpid(), i))
        x.put('pid{} {}'.format(os.getpid(), i))


def consume(x):
    for i in range(10):
        time.sleep(1)
        print('{} 消费了{}'.format(os.getpid(), x.get()))


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=produce, args=(q,))
    p1.start()

    c1 = multiprocessing.Process(target=consume, args=(q,))
    c1.start()
