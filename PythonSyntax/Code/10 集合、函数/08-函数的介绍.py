# 函数就是一堆准备好的代码，在需要的时候调用这一堆代码

# 缺点：冗余、可读性差、维护性差

# 把多行代码封装成一个整体（函数）
# 在Python里，使用关键字 def 来声明一个函数

# def 函数名(参数)：
#   函数要执行的操作

# 函数定义好了以后并不会自动执行
def tell_story():
    print('从前有座山')
    print('山上有座庙')
    print('庙里有个老和尚')
    print('还有一个小和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是')


age = int(input('请输入孩子年龄'))
if 0 <= age < 3:
    for i in range(0, 5):
        tell_story()  # 函数名(参数)
elif 3 <= age < 5:
    tell_story()
