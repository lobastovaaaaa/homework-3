from shape import Shape
import random


class Parall(Shape):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.width = 0
        self.height = 0

    def fill(self, str_array, i):
        if i >= len(str_array) - 2:
            return 0
        self.length = int(str_array[i])
        self.width = int(str_array[i + 1])
        self.height = int(str_array[i + 2])
        i += 3
        return i

    def random_fill(self):
        self.length = random.randint(1, 20) + round(random.random(), 4)
        self.width = random.randint(1, 20) + round(random.random(), 4)
        self.height = random.randint(1, 20) + round(random.random(), 4)

    def print(self):
        print("Parallelepiped: length = {}, width = {}, height = {}."
              " Surface area = {}.".format(self.length, self.width, self.height, self.surface_area()))

    def write(self, ostream):
        ostream.write("Parallelepiped: length = {}, width = {}, height = {}."
                      " Surface area = {}.".format(self.length, self.width, self.height, self.surface_area()))

    def surface_area(self):
        return round(self.length * self.width * self.height, 4)
