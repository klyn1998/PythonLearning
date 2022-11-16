# 房子（House）有户型、总面积、剩余面积（等于总面积的60%） 和 家具名称列表 属性
# 新房子没有任何的家具
# 将 家具的名称 追加到 家具名称列表 中
# 判断 家具的面积 是否超过 剩余面积，如果超过，提示不能添加这件家具


class House(object):
    def __init__(self, house_type, total_area, fur_list=None):
        if fur_list is None:  # 缺省参数
            fur_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fur_list = fur_list

    def add_fur(self, furniture):
        if self.free_area - furniture.area < 0:
            print('无法添加！')
        else:
            self.fur_list.append(furniture.name)
            self.free_area -= furniture.area

    def __str__(self):
        return '户型：{}，总面积：{}，剩余面积：{}，家具列表：{}'.format(self.house_type, self.total_area, self.free_area,
                                                                  self.fur_list)


# 家具（HouseItem）有 名字 和占地面积属性，其中
# bed 占地 4 平米
# closet 占地 2 平米
# table 占地 1.5 平米
# 将以上三件 家具 添加到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具列表名称


class HouseItem(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


bed = HouseItem('bed', 10)
closet = HouseItem('closet', 2)
table = HouseItem('table', 1.5)

new_house = House('villa', 320)
# 把家具添加到房间里（面向对象关注点：让谁做）

new_house.add_fur(bed)
new_house.add_fur(closet)
new_house.add_fur(table)

# print打印一个对象的时候，会调用这个对象的__repr__或者__str__方法，获取它们的返回值
print(new_house)
