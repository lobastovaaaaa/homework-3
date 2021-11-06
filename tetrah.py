from shape import Shape
import random


class Tetrah(Shape):
    def __init__(self):
        super().__init__()
        self.edge = 0

    def fill(self, str_array, i):
        if i >= len(str_array):
            return 0
        self.edge = int(str_array[i])
        i += 1
        return i

    def random_fill(self):
        self.edge = random.randint(1, 20) + round(random.random(), 4)

    def print(self):
        print("Tetrahedron: edge = {}. Surface area = {}.".format(self.edge, self.surface_area()))
        pass

    def write(self, ostream):
        ostream.write("Tetrahedron: edge = {}. Surface area = {}.".format(self.edge, self.surface_area()))
        pass

    def surface_area(self):
        return round(1.732 * self.edge * self.edge, 4)
