# 魔法（魔术）方法，是类里的特殊的一些方法
# 特点：
# 1. 不需要手动调用，会在合适的时机自动调用
# 2. 这些方法，都是使用 __ 开始，使用 __ 结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用
# import time
import datetime

x = datetime.datetime(2022, 10, 15, 13, 50, 12, 200)
print(x)  # __str__ 方法
print(repr(x))  # __repr__ 方法


class Person:
    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        # 自动销毁
        print('__del__方法被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return 'name:{}, age:{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print('call方法被调用了')
        # args是一个元祖
        # kwargs是一个字典
        print(args, kwargs)
        fn = kwargs['fn']
        return fn(args[0], args[1])


p = Person('allen', 18)

# del p  # 手动销毁
# time.sleep(3)

# 如果不做任何修改，直接打印一个对象，是对象的 模块名.类 及内存地址
# print(p)  # <__main__.Person object at 0x7fef37b1dfd0>

# 当打印一个对象的时候，会调用对象的 __str__ 或者 __repr__ 方法
# 如果两个方法都写了，选择 __str__
print(p)

print(repr(p))  # 调用内置函数 repr 会触发对象的 __repr__ 方法
# print(p.__repr__())  # 魔法方法，一般不手动调用

# 对象名() ==> 调用对象的 __call__ 方法
print(p(1, 2, fn=lambda a, b: a + b))
