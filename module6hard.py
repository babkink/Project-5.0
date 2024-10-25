from math import pi
class Figure:
    sides_count = 0
    __sides = [3,4]
    __color = [10, 10, 10]
    filled = True
    def __init__(self, color, sides, filled = True):
        self.__sides = sides
        self.__color = color
        self.filled = filled
        if isinstance(self.__sides, int):
            # if self.__sides != self.sides_count:
            self.__sides = [self.__sides] * self.sides_count
        else:
            if len(self.__sides) != self.sides_count:
                    self.__sides = [1] * self.sides_count
            if self.sides_count == 12:
                if not all(i == self.__sides[0] for i in self.__sides):
                    self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self.__color

    def __is_valid_sides(self, ar):
        for i in range(len(ar)):
            if ar[i] <= 0:
                return False
        if len(ar) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def _len_(self):
        return sum(self.get_sides())

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)
        else:
            self.__sides = [1] * self.sides_count

    def __len__(self):
        return sum(self.get_sides())

class Circle(Figure):
    sides_count = 1

    def __radius(self):
        a = self.get_sides()
        return a[0] / (2 * pi)

    def get_radius(self):
        return self.__radius()

    def get_square(self):
        a = self.get_sides()
        return a[0] ** 2 / (4 * pi)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5



class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        side = self.get_sides()
        return side[0] ** 3


triangle = Triangle((100, 100, 100), 2)
print(triangle.get_sides())
print(triangle.sides_count)
triangle.set_sides(4, 4)
print(triangle.get_sides())