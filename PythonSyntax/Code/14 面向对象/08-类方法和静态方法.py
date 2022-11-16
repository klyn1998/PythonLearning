class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b


print(Calc.add(1, 2))
print(Calc.sub(1, 2))


class Person:
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 对象方法有一个参数self，指的是实例对象
        print(self.name + '正在吃' + food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法定义为static
    @staticmethod
    def demo():  # 默认的方法都是对象方法
        print('hello')

    @classmethod
    def test(cls):
        # 类方法会有一个参数 cls，也不需要手动传参，会自动传参
        # cls 指的是类对象  cls is Person
        print(cls.type)


p1 = Person('allen', 18)
# 实例对象在调用方法时，不需要给形参self传参，会自动把实例对象传递给self
p2 = Person('bob', 19)

# eat 对象方法，可以直接使用实例对象.方法名（参数）调用
# 使用对象名.方法名（参数）调用的方式，不需要传递self
# 会自动将对象名传递给self
p1.eat('watermelon')  # 直接使用实例对象调用方法

# 对象方法还可以使用 类对象来调用 类名.方法名()
# 这种方式，不会自动给self传参，需要手动的指定self
Person.eat(p2, 'orange')

print(p1.eat)
print(p2.eat)
print(Person.eat)

# 静态方法：没有用到实例对象的任何属性；可以使用实例对象和类对象调用
Person.demo()
p1.demo()

# 类方法：可以使用实例对象和类对象调用
Person.test()
p1.test()
