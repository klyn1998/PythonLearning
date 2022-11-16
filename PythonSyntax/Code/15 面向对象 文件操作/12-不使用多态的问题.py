# 多态是基于继承，通过子类重写父类的方法
# 达到不同的子类对象调用相同的父类方法，得到不同的结果
# 提高代码的灵活度

class PoliceDog:
    @staticmethod
    def attack_enemy():
        print('警犬咬人')


class BlindDog:
    @staticmethod
    def lead_road():
        print('盲犬领路')


class DrugDog:
    @staticmethod
    def search_drug():
        print('缉毒犬在搜毒')


class Person:
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_pd(self):
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.lead_road()

    def work_with_dd(self):
        self.dog.search_drug()


p = Person('allen')

pd = PoliceDog()
p.dog = pd
p.work_with_pd()

bd = BlindDog()
p.dog = bd
p.work_with_bd()

dd = DrugDog()
p.dog = dd
p.work_with_dd()
