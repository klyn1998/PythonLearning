class Person(object):
    def __init__(self, name, age):  # self 在创建对象时才会调用
        self.name = name
        self.age = age

    def eat(self):  # 执行时才会调用
        print(self.name + '正在吃东西')


p1 = Person('allen', 18)
p2 = Person('bob', 20)
