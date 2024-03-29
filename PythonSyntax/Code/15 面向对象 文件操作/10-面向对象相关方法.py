class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class X:
    pass


class Student(Person):
    pass


p1 = Person('allen', 18)
p2 = Person('bob', 18)

s = Student('jack', 20)

# 获取两个对象的内存地址  id(p1) == id(p2)
print(p1 is p2)  # is 身份运算符是用来比较两个对象是否是同一个对象

print(type(p1))  # 其实获取的就是类对象
print(type(1) == int)  # True
print(type(p1) == Person)  # True

# s这个实例对象是否是由Student类创建的？
print(type(s))
print(type(s) == Student)  # True
print(type(s) == Person)  # False

# isinstance 用来判断一个对象是否是由指定的类（或父类）实例化出来的
print(isinstance(s, (Student, X)))  # True
print(isinstance(s, Person))  # True

print(isinstance(p1, Person))  # True
print(isinstance(p1, Student))  # False

# issubclass 用来判断一个类是否是另一个类的子类
print(issubclass(Student, (Person, X)))  # True
print(issubclass(Person, Student))  # False
