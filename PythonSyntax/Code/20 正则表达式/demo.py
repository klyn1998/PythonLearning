class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '正在吃' + food)

    def sleep(self):
        print(self.name + '正在睡觉')


_p = Person('allen')
eat = _p.eat  # 给对象的eat方法设置一个别名
