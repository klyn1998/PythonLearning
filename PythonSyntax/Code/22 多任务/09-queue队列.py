import multiprocessing
import queue

# q1 = multiprocessing.Queue()  # 进程间通信
# q2 = queue.Queue()  # 线程间通信

# 创建队列时，可以指定最大长度。默认值是0，表示不限
q = multiprocessing.Queue(5)

q.put('hello')
q.put('ok')
q.put('good')
q.put('morning')
q.put('bad')

# print(q.full())
# block=True：表示是阻塞的，如果队列已经满了，就等待
# timeout：超时，等待多久之后程序会出错，单位是秒
# q.put('a', block=True, timeout=3)

# q.put_nowait('how')  # 等价于q.put('how', block=False)

# block, timeout, nowait 同理
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get_nowait())



