import math
from math import pi


class Figure:
    sides_count = 0

    def __init__(self, __color: tuple[int, int, int], *__sides: int):
        self.filled = 0
        self.color = __color
        self.sides = __sides
        self.sides_num_check()

    def get_color(self):
        return self.color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and r in range(0, 256):
            if isinstance(g, int) and g in range(0, 256):
                if isinstance(b, int) and b in range(0, 256):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = list(self.color)
            self.color[0] = r
            self.color[1] = g
            self.color[2] = b
            self.color = tuple(self.color)
        else:
            pass

    def __is_valid_sides(self, *args):
        check_args = False
        check_sides = False
        for i in args:
            if isinstance(i, int) and i > 0:
                check_args = True
            else:
                check_args = False
                break
        if len(args) == len(self.sides):
            check_sides = True
        if check_sides and check_args:
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = new_sides

    def get_sides(self):
        return list(self.sides)

    def __len__(self):
        result = 0
        for i in range(0, len(self.sides)):
            result += self.sides[i]
        return result

    def sides_num_check(self):
        if len(self.sides) != self.sides_count:
            tech_sides = []
            while len(tech_sides) != self.sides_count:
                tech_sides.append(1)
            self.sides = tech_sides
        return self.sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color: tuple[int, int, int], *__sides: int):
        super().__init__(__color, *__sides)
        self.color = __color
        self.sides = __sides
        self.sides_num_check()
        self.radius = len(self.sides) / (2 * pi)

    def get_square(self):
        return print(pi * (self.radius ** 2))


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color: tuple[int, int, int], *__sides: int):
        super().__init__(__color, *__sides)
        self.color = __color
        self.sides = __sides
        self.sides_num_check()
        self.height = math.sqrt((len(self) / 2) * ((len(self) / 2)
                                                   - self.sides[0]) * ((len(self) / 2)
                                                                       - self.sides[1]) * ((len(self) / 2)
                                                                                           - self.sides[2])) / \
                      self.sides[0]

    def get_square(self):
        return math.sqrt((len(self) / 2) * ((len(self) / 2) - self.sides[0]) * ((len(self) / 2) - self.sides[1]) * (
                (len(self) / 2) - self.sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color: tuple[int, int, int], *sides: int):
        super().__init__(__color, *sides)
        self.color = __color
        self.sides = sides
        self.__modify_cube(*sides)

    def __modify_cube(self, *sides):
        mod_side = []
        if len(sides) > 1:
            sides = 1
        else:
            sides = sides[0]
        while len(mod_side) != self.sides_count:
            mod_side.append(sides)
        self.sides = mod_side
        return self.sides

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
