import sys

# sys.stdin  接收用户的输入，读取键盘里输入的数据
# sys.stdout 标准输出
# sys.stderr 错误输出
# 默认都是控制台


s_in = sys.stdin  # input 就是读取 sys.stdin 里的数据
while True:
    content = s_in.readline().rstrip('\n')
    if not content:
        break
    print(content)

# sys.stdout = open('stdout.txt', 'w')
# print('hello')
# print('yes')
# print('good')
#
# sys.stderr = open('stderr.txt', 'w')
# print(1 / 0)
