from math import pi, sqrt


# 定义一个点类 Point
# 属性是横向坐标x 与纵向坐标y
# 定义一个圆类 Circle
# 属性有圆心cp 与半径 radius
# 方法有：
# 1. 求圆的面积
# 2. 求圆的周长
# 3. 求指定点与圆的关系
# tips：关系有三种 圆内，圆外，圆上
# 涉及到的数学公式：指定点与圆心点之间的距离 与 圆的半径进行比较
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, cp: Point, radius):
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_relation(self, p):
        distance = (p.x - self.cp.x) ** 2 + (p.y - self.cp.y) ** 2
        if distance < self.radius ** 2:
            return '在圆内'
        elif distance == self.radius ** 2:
            return '在圆上'
        else:
            return '在圆外'


p1 = Point(1, 5)
cp1 = Point(1, 1)
c1 = Circle(cp1, 2)
print(c1.get_area())
print(c1.get_relation(p1))
