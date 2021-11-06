from shape import Shape
import random


class Sphere(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def fill(self, str_array, i):
        if i >= len(str_array):
            return 0
        self.radius = int(str_array[i])
        i += 1
        return i

    def random_fill(self):
        self.radius = random.randint(1, 20) + round(random.random(), 4)

    def print(self):
        print("Sphere: radius = {}. Surface area = {}.".format(self.radius, self.surface_area()))
        pass

    def write(self, ostream):
        ostream.write("Sphere: radius = {}. Surface area = {}.".format(self.radius, self.surface_area()))
        pass

    def surface_area(self):
        return round(4 * self.radius * self.radius * 3.14159, 4)
