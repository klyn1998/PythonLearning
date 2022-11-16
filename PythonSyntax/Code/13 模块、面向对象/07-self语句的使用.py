class Student:
    # 这个属性直接定义在类里，是一个元祖，用来规定对象可以存在的属性
    __slots__ = ('name', 'age', 'city')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是{}'.format(self.name))


# Student('allen', 18) 这段代码具体做了什么？
# 1. 调用__new__方法，用来申请内存空间
# 2. 调用__init__方法传入参数，将self指向创建好的内存空间，填充数据
# 3. 变量s1也指向创建好的内存空间
s1 = Student('allen', 18)
s1.say_hello()

# 没有属性，会报错
# print(s1.height)

# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 动态属性
s1.city = 'Shanghai'  # 给对象添加了一个city属性
print(s1.city)

# 如果这个属性以前存在，会修改这个属性对应的值
s1.name = 'jack'
print(s1.name)  # jack

