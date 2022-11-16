import threading
import time

ticket = 20
# 创建一把锁
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        lock.acquire()  # 加同步锁
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            lock.release()
            print('{}卖出一张票，还剩{}张票'.format(threading.currentThread().name, ticket))
        else:
            lock.release()
            print('票卖完了')
            break


t1 = threading.Thread(target=sell_ticket, name='thread1')
t2 = threading.Thread(target=sell_ticket, name='thread2')
t1.start()
t2.start()
