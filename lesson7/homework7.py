# Задача 1
class Matrix:
    def __init__(self, list_listov):
        self.list_listov = list_listov

    def __str__(self):
        ret_str = ""
        for el in self.list_listov:
            ret_str += el.__str__() + "\n"
        return ret_str

    def __add__(self, other):
        i_size = len(self.list_listov)
        j_size = len(self.list_listov[0])
        ret_m = []
        for i in range(i_size):
            ret_m.append([])
            for j in range(j_size):
                ret_m[i].append(0)
                ret_m[i][j] = self.list_listov[i][j] + other.list_listov[i][j]
        return Matrix(ret_m)


mx = Matrix([[2, 1, 2], [3, 4, 5], [1, 2, 3]])
mx_1 = Matrix([[4, 2, 8], [5, 7, 8], [0, 6, 1]])
print(mx)
print(mx_1)
print(mx + mx_1)

# Задача 2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @property
    def mats_cost(self):
        return f'Общий расход ткани: {(self.size / 6.5 + 0.5) + (2 * self.growth + 0.3):.2f} метров'


class Coat(Clothes):

    @property
    def mats_cost(self):
        return f'Расход ткани на пальто: {self.size / 6.5 + 0.5:.2f}'


class Costume(Clothes):

    @property
    def mats_cost(self):
        return f'Расход ткани на костюм: {2 * self.growth + 0.3:.2f}'


general = Clothes(36, 170)
cl = Coat(36, 170)
cst = Costume(36, 170)
print(cl.mats_cost)
print(cst.mats_cost)
print(general.mats_cost)


# Задача 3
import sys


class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return str(self.quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            raise Exception("Мало клеток")

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cell_count):
        ret_str = ""
        for i in range(self.quantity // cell_count):
            for j in range(cell_count):
                ret_str += "*"
            ret_str += "\n"
        for j in range(self.quantity % cell_count):
            ret_str += "*"
        ret_str += "."
        return ret_str


cell_1 = Cell(25)
cell_2 = Cell(3)
cell_3 = Cell(3)
print(cell_1 + cell_2 + cell_3)

try:
    print(cell_2 - cell_1)
    print(cell_1 - cell_2)
except Exception:
    print("Исключение: ", sys.exc_info()[1])

print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))

