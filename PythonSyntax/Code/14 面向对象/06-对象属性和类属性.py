class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象 p1和p2 是通过 Person 类创建出来的实例对象
# name 和 age 是对象属性，是每一个实例对象都会单独保存一份的属性
# 每个实例对象之间的属性没有关联，互不影响
p1 = Person('allen', 18)
p2 = Person('bob', 19)
print('0x%X, 0x%X' % (id(p1), id(p2)))

# Person 我们称之为类对象
print('0x%X' % id(Person))

x = p1
print(x.name)

# 类属性可以通过类对象和实例对象获取
print(Person.type)
print(p1.type)
print(p2.type)

# 类属性只能通过类对象来修改，实例对象无法修改类属性
p1.type = 'human'  # 并不会修改类属性，而是给实例对象新增一个对象属性
print(p1.type)
print(p2.type)

Person.type = 'monkey'  # 修改类属性
print(Person.type)  # monkey
print(p2.type)  # monkey
print(p1.type)  # human
