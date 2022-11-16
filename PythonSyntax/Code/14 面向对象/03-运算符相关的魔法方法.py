class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):  # 使用!=运算符会自动调用这个方法
        return 'hello'

    def __gt__(self, other):  # greater than 使用 > 会自动调用这个方法
        return self.age > other.age

    def __ge__(self, other):  # 使用 >= 会自动调用
        return self.age >= other.age

    def __lt__(self, other):  # less than p1 < p2
        pass

    def __le__(self, other):  # <=
        pass

    def __add__(self, other):  # +
        return self.age + other.age

    def __sub__(self, other):  # -
        return self.age - other.age

    def __mul__(self, other):  # *
        return self.age * other

    def __truediv__(self, other):  # /
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __str__(self):
        return 'hello'

    def __int__(self):
        return int(p1.age)

    def __float__(self):
        return float(p1.age)


p1 = Person('allen', 18)
p2 = Person('allen', 18)
p3 = Person('bob', 19)
print(p1 is p2)  # False

# == 运算符本质是调用对象的__eq__方法，获取__eq__方法的返回结果
# a == b => a.__eq__(b)
print(p1 == p2)  # True  p1.__eq__(p2)

# != 本质是调用__ne__方法，或者__eq__方法取反
print(p1 != p2)  # False

print(p1 > p3)

print(p1 >= p2)

print(p1 * 2)

# str() 将对象转换成为字符串，会自动调用 __str__ 方法
# 1. str()  2. 打印对象也会调用
print(str(p1))  # 转换成为字符串。默认转换成为类型+内存地址
print(p1)

# print(int('1234'))  # 调用对象的__int__方法
print(int(p1))

print(float(p1))
