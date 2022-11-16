import time
import threading
import queue


def produce():
    for i in range(10):
        time.sleep(0.5)
        print('生产了面包{} {}'.format(threading.currentThread().name, i))
        q.put('{}{}'.format(threading.currentThread().name, i))


def consume():
    while True:
        time.sleep(1)
        print('{}购买了面包{}'.format(threading.currentThread().name, q.get()))


q = queue.Queue()

pa = threading.Thread(target=produce, name='pa')
pb = threading.Thread(target=produce, name='pb')
pc = threading.Thread(target=produce, name='pc')

ca = threading.Thread(target=consume, name='ca')
cb = threading.Thread(target=consume, name='cb')
cc = threading.Thread(target=consume, name='cc')

pa.start()
pb.start()
pc.start()

ca.start()
cb.start()
cc.start()
