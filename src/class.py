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

if __name__ == "__main__":
    f = StringFileIterator('abc', 3)
    print(list(f))