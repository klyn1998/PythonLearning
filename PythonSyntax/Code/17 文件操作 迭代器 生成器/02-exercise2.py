from math import pi


class Point:
    def __init__(self, coordinate):
        self.coordinate = coordinate


class Circle:
    def __init__(self, cp: Point, radius):
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_relation(self, p):
        distance = (p.coordinate[0] - self.cp.coordinate[0]) ** 2 + (p.coordinate[1] - self.cp.coordinate[1]) ** 2
        if distance < self.radius ** 2:
            return '在圆内'
        elif distance == self.radius ** 2:
            return '在圆上'
        else:
            return '在圆外'


p1 = Point((0, 5))
cp1 = Point((0, 0))
c1 = Circle(cp1, 5)
print(c1.get_relation(p1))
