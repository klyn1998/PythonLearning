class Dog:
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击')


class BlindDog(Dog):
    def work(self):
        print('导盲犬在领路')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬在缉毒')


class Person:
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


p = Person('allen')

pd = PoliceDog()
p.dog = pd
p.work_with_dog()

bd = BlindDog()
p.dog = bd
p.work_with_dog()

dd = DrugDog()
p.dog = dd
p.work_with_dog()
