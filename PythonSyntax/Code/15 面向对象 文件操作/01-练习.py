# 定义一个类属性，记录通过这个类创建了多少个对象
class Person:
    __count = 0  # 类属性

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return object.__new__(cls)  # 申请内存，创建一个对象，并设置类型是 Person 类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count


# 每次创建对象，都会调用__new__和__init__方法
# 调用__new__方法，用来申请内存
# 如果不重写__new__方法，会自动找object 的 __new__
# object的__new__方法，默认实现申请了一段内存，创建一个对象

p1 = Person('allen', 19)
p2 = Person('bob', 20)
p3 = Person('cindy', 23)

p4 = object.__new__(Person)  # 申请了内存，创建了一个对象，并设置它的类型是Person
p4.__init__('tony', 23)

print(Person.get_count())
