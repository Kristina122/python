# Задача № 1.
from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def __str__(self):
        return self.__color

    def running(self):
        print(self)
        if self.__color == "RED":
            sleep(7)
            self.__color = "YELLOW"
        print(self)
        if self.__color == "YELLOW":
            sleep(3)
            self.__color = "GREEN"
        print(self)
        if self.__color == "GREEN":
            sleep(5)
            self.__color = "RED"


traffic_light = TrafficLight("RED")
traffic_light.running()

# 2.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, weight, thickness):
        return self._length * self._width * weight * thickness


road_1 = Road(10, 25)
s = road_1.calc(2, 5)
print(s)


# 3.


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker = Position("Ivan", "Petrov", "engineer", {"wage": 10000, "bonus": 1000})
print(worker.get_full_name())
print(worker.get_total_income())

# 4.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        return f"Скорость: {self.speed}, цвет: {self.color}, имя: {self.name}, полиция:{self.is_police}"

    def show_speed(self):
        print(self.speed)
        return self.speed

    def go(self):
        if self.speed > 0:
            print("Машина поехала")

    def stop(self):
        if self.speed == 0:
            print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость больше 40 км.ч.")


class PoliceCar(Car):
    pass


car_1 = TownCar(66, "white", "Audi", False)
car_1.show_speed()
print(car_1)
car_1.go()
car_1.speed = 0
car_1.stop()
print(car_1.name)

car_2 = WorkCar(56, "black", "Toyota", False)
car_2.show_speed()
print(car_2)
car_2.turn("left")
print(car_2.speed)

# Задача 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Ручка")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш")


class Handle(Stationery):
    def draw(self):
        print("Маркер")


pen = Pen("pen")
pencil = Pencil("pencil")
handle = Handle("handle")

pen.draw()
pencil.draw()
handle.draw()