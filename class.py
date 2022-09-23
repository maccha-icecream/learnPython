import sys

class Book:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

if __name__ == '__main__':
    book = Book("戦争と平和")
    # book.name = "戦争は女の顔をしていない"
    print(book.getName())