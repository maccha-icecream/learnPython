"""
ダックタイピング
"""
from math import pi


class Rectangle:
    """
    四角形クラス
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width / 2



class Circle:
    """
    円クラス
    """
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * pi


def print_area(shape):
    print(f"Area of this shape is {shape.get_area()}")


class Duck:
    """
    アヒルクラス
    """
    def sound(self):
        return 'quack'


class Cat:
    """
    猫クラス
    """
    def sound(self):
        return 'myaa'


def duck_typing_test(animal):
    print(animal.sound())


if __name__ == "__main__":
    rectangle = Rectangle(10, 10)
    circle = Circle(3)
    print_area(rectangle)
    print_area(circle)

    duck = Duck()
    cat = Cat()
    duck_typing_test(duck)
    duck_typing_test(cat)

