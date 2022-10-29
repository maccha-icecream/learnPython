import sys

class HelloForEver:
    def readline(self):
        return 'Hello. \n'

class HelloFine:
    def __init__(self, n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return 'Hello. \n'

class HelloFile(HelloForEver):
    def __init__(self, n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return super().readline()


class HelloFileIterator(HelloFile):
    def __iter__(self):
        return self
    def __next__(self):
        line = self.readline()
        if line == '':
            raise StopIteration
        return line


class StringFileIterator(HelloFileIterator):
    def __init__(self, s, n):
        self.s = s
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return self.s

class Person(object):
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print(f'I\'m {self.name}.')
        self.run(3)

    def run(self, num):
        print('run' * num)

    # デストラクタ
    def __del__(self):
        print('good bye')


class Car:
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print('Run')


class ToyotaCar(Car):
    def __init__(self, model = "Model S", enable_auto_run = False):
        super().__init__()
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self.__enable_auto_run = is_enable

    def run(self):
        print('fast')

class TeslaCar(Car):
    def auto_run(self):
        print('Auto run')

    def run(self):
        print('Super fast')


import math


class Point:

    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count += 1
        print(f"you made {Point.count} instance(s).")


    def __str__(self):
        return f"(x, y) = ({self.x}, {self.y})"

    @classmethod
    def create_origin(cls):
        return cls(0, 0)

    @staticmethod
    def calc_dist(point1, point2):
        x = point1.x - point2.x
        y = point1.y - point2.y
        return math.sqrt(x ** 2 + y ** 2)

class Word:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"This is {self.text}."

    def __len__(self):
        return len(self.text)

    def __add__(self, other):
        return self.text.lower() + other.text.lower()

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()


if __name__ == "__main__":
    word = Word('test')
    word2 = Word('test')

    print(word)
    print(len(word))
    print(word + word2)
    print(word == word2)
