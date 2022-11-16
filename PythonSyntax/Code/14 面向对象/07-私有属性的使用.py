import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def add_money(self):
        self.__money += 10  # 在这里可以访问私有属性

    def get_money(self):
        print('{}查询了余额'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, balance):
        if type(balance) != int:
            print('设置余额不合法')
            return
        print('修改余额了')
        self.__money = balance

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print('我是demo函数，name: {}'.format(self.name))

    def test(self):
        self.__demo()


p = Person('allen', 18)
print(p.name, p.age)  # 可以直接获取
# print(p.__money)  # 不能直接获取到私有变量
# p.add_money()

# p.__demo()  # 不能直接调用demo，它是私有方法
p._Person__demo()
p.test()

# 获取私有变量的方式：
# 1. 使用 对象._类名__私有变量名获取
print(p._Person__money)

# 2. 定义get和set方法来获取
print(p.get_money())
p.set_money(1100)
print(p.get_money())

# 3. 使用property来获取
