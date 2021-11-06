from parall import Parall
from sphere import Sphere
from tetrah import Tetrah
import random


class Container:
    def __init__(self):
        self.store = []
        pass

    def fill(self, array):
        array_len = len(array)
        i = 1
        fig_num = 0
        while i < array_len:
            new_str = array[i]
            key = int(new_str)
            if key == 1:
                shape = Sphere()
            elif key == 2:
                shape = Tetrah()
            elif key == 3:
                shape = Parall()
            else:
                return fig_num
            if key == 1 or key == 2 or key == 3:
                i += 1
                i = shape.fill(array, i)
            if i == 0:
                return fig_num
            fig_num += 1
            self.store.append(shape)
        return fig_num

    def random_fill(self, number):
        for i in range(number):
            key = random.randint(1, 3)
            if key == 1:
                shape = Sphere()
            elif key == 2:
                shape = Tetrah()
            elif key == 3:
                shape = Parall()
            shape.random_fill()
            self.store.append(shape)

    def sort(self):
        for i in range(len(self.store) - 1):
            for j in range(len(self.store) - 2, i - 1, -1):
                if self.store[j].surface_area() > self.store[j + 1].surface_area():
                    tmp = self.store[j]
                    self.store[j] = self.store[j + 1]
                    self.store[j + 1] = tmp

    def surface_area_sum(self):
        sum_areas = 0
        for shape in self.store:
            sum_areas += shape.surface_area()
        return round(sum_areas, 4)

    def print(self):
        print('Container contains {} objects.\n\n'.format(len(self.store)))
        for shape in self.store:
            shape.print()
        print('\nSurface area sum = ', self.surface_area_sum())

    def write(self, ostream):
        ostream.write('Container contains {} objects.\n\n'.format(len(self.store)))
        for shape in self.store:
            shape.write(ostream)
            ostream.write('\n')
        ostream.write('\nSurface area sum = {}'.format(self.surface_area_sum()))

    def write_sorted(self, ostream):
        self.sort()
        ostream.write('Sorted container contains {} objects.\n\n'.format(len(self.store)))
        for shape in self.store:
            shape.write(ostream)
            ostream.write('\n')
        ostream.write('\nSurface area sum = {}'.format(self.surface_area_sum()))
