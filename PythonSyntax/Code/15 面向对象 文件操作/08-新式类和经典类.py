# 手动指定Student类继承自object
class Student(object):  # 兼容性问题
    pass


# 没有指定Dog的父类，Python3里默认继承自object
class Dog:
    pass

# 新式类和经典类的概念
# 1. 新式类：继承自 object 的类我们称之为新式类
# 2. 经典类：不继承自object的类

# 在Python2里，如果不手动指定一个类的父类是object，这个类是经典类
# Python3里不存在经典类，都是新式类

