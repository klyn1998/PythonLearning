# 宠物店类 PetShop
# 属性：店名，店中的宠物（使用列表存储宠物）
# 方法：展示所有宠物的信息

# 宠物狗类 PetDog
# 属性：昵称，性别，年龄，品种
# 方法：叫，拆家，吃饭

# 宠物猫类：PetCat
# 属性：昵称，性别，年龄，品种，眼睛的颜色
# 方法：叫，撒娇，吃饭

# tips：狗的叫声是汪汪 猫的叫声是喵喵
#      狗吃的是骨头 猫吃的是鱼
class PetShop:
    def __init__(self, name, pet_list=None):
        self.name = name
        if pet_list is None:
            pet_list = []
        self.pet_list = pet_list

    def show_pets(self):
        if len(self.pet_list) == 0:
            print('本店还没有宠物')
            return
        print(self.pet_list)


class Pet:
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def bark(self):
        print(self.name + '正在叫')

    def play(self):
        print(self.name + '正在玩')

    def eat(self):
        print(self.name + '正在吃')

    def __repr__(self):
        return '姓名：{}，性别：{}，年龄：{}，品种：{}'.format(self.name, self.gender, self.age, self.breed)


class PetDog(Pet):
    def __init__(self, name, gender, age, breed):
        super(PetDog, self).__init__(name, gender, age, breed)

    def bark(self):
        print(self.name + '正在汪汪叫')

    def play(self):
        print(self.name + '正在拆家')

    def eat(self):
        print(self.name + '正在吃骨头')


class PetCat(Pet):
    def __init__(self, name, gender, age, breed, eyes_color):
        super(PetCat, self).__init__(name, gender, age, breed)
        self.eyes_color = eyes_color

    def bark(self):
        print(self.name + '正在喵喵叫')

    def play(self):
        print(self.name + '正在撒娇')

    def eat(self):
        print(self.name + '正在吃鱼')

    def __repr__(self):
        x = super(PetCat, self).__repr__()
        x += '，眼睛颜色：{}'.format(self.eyes_color)
        return x


pd1 = PetDog('doge', 'male', 3, 'corky')
pd2 = PetDog('jerry', 'female', 7, 'blackdog')
pc1 = PetCat('kitty', 'male', 2, 'American', 'blue')
pc2 = PetCat('tom', 'female', 4, 'English', 'yellow')
ps = PetShop('cat_lover', [pd1, pd2, pc1, pc2])
ps.show_pets()
