# Лабораторная работа №8, вариант 2
# Фигуры: абстрактный базовый класс Shape и наследники Circle, Rectangle, Triangle

from abc import ABC, abstractmethod
import math


# Абстрактный базовый класс с обязательными для наследников методами
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"{self.name}: площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Круг"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = "Прямоугольник"

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = "Треугольник"

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Ввод положительного числа с проверкой
def read_number(text):
    while True:
        try:
            value = float(input(text))
        except ValueError:
            print("Нужно ввести число")
            continue
        if value <= 0:
            print("Число должно быть положительным")
            continue
        return value


def main():
    shapes = []

    shapes.append(Circle(read_number("Радиус круга: ")))

    a = read_number("Сторона a прямоугольника: ")
    b = read_number("Сторона b прямоугольника: ")
    shapes.append(Rectangle(a, b))

    # Треугольник вводим, пока не выполняется неравенство треугольника
    while True:
        a = read_number("Сторона a треугольника: ")
        b = read_number("Сторона b треугольника: ")
        c = read_number("Сторона c треугольника: ")
        if a + b > c and a + c > b and b + c > a:
            shapes.append(Triangle(a, b, c))
            break
        print("Такого треугольника не существует, попробуйте снова")

    # Полиморфизм: обходим общий список объектов базового типа
    for shape in shapes:
        print(shape)


main()
