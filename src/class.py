import sys
from decimal import Decimal
class Book:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

class Money:
    def __init__(self, amount):
        self.__amount = Decimal(amount)
    def getAmount(self):
        return self.__amount
    def add(self, other):
        str1 = '{0:f}'.format(self.__amount + other.getAmount())
        return Money(str1)

    def subtract(self, other):
        str1 = '{0:f}'.format(self.__amount - other.getAmount())
        return Money(str1)

if __name__ == '__main__':
    book = Book("戦争は女の顔をしていない")
    print(book.getName())
    print(book._Book__name)

    money = Decimal("0.1")
    other = Decimal("0.7")
    added = money + other
    print(type(added))

    money = Money("0.1")
    other = Money("0.2")
    added = money.add(other)
    print(added.getAmount())

    subtract = money.subtract(other)
    print(subtract.getAmount())
