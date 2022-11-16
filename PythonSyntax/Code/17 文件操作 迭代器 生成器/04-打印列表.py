class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.age)


p1 = Person('allen', 18)
p2 = Person('bob', 20)

persons = [p1, p2]
# 直接打印列表，会调用列表里元素的__repr__方法
print(persons)
