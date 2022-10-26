l = ['Good morning', 'Good afternoon', 'Good Night']


def greeting():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good Night'


def counter(num = 10):
    for _ in range(num):
        yield 'run'


g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print('Hi, I\'m here.')
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
