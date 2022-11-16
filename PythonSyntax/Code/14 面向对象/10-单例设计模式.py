class Singleton:
    __instance = None  # 类属性
    __is_first = True

    def __new__(cls, *args, **kwargs):
        # 申请内存，创建一个对象，并把对象的类设置为cls
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first is True:
            self.a = a
            self.b = b
            self.__is_first = False


# 调用 __new__ 方法申请内存
# 如果不重写 __new__ 方法，会调用 object 的 __new__ 方法 ==> 申请内存
# 如果重写了 __new__ 方法，需要自己手动申请内存
s1 = Singleton('aaa', 'bbb')
s2 = Singleton('ccc', 'ddd')
s3 = Singleton('eee', 'fff')

print(s1.a, s2.a)
print(s1.b, s2.b)

print(s1 is s2)  # True
print(s1, s2)
