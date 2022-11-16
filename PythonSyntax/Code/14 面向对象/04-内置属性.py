class Person(object):
    """
    这是一个人类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


# 'name': 'allen', 'age' :18, 'eat': <function>
p = Person('allen', 18)
print(p.__doc__)

print(dir(p))
print(p.__class__)  # <class '__main__.Person'>
print(p.__dict__)  # {'name': 'allen', 'age': 18} 把对象属性和值转换成为一个字典
print(p.__dir__())  # 等价于 dir(p)
print(p.__doc__)  # 对象名.__doc__
print(range.__doc__)  # 类名.__doc__
print(p.__module__)  # __main__
