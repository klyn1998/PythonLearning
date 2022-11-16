# 设计两个类：
# - 一个点类，属性包括x, y坐标
# - 一个Rectangle类（矩形），属性有左上角和右下角的坐标
# 方法：1. 计算矩形的面积；2. 判断点是否在矩形内
# 实例化一个点对象，一个正方形对象，输出矩形的面积，输出点是否在矩形内

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def area(self):
        length = self.bottom_right.x - self.top_left.x
        width = self.top_left.y - self.bottom_right.y
        return length * width

    def is_in_rectangle(self, point):
        return self.top_left.x <= point.x <= self.bottom_right.x and self.bottom_right.y <= point.y <= self.top_left.y


p1 = Point(5, 10)
p2 = Point(20, 3)
r = Rectangle(p1, p2)
print(r.area())

p = Point(14, 7)
print(r.is_in_rectangle(p))
