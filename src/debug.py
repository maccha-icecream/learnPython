import sys


def square(x):
    # return x ** 2
    return x + x


# assert  square(-2) >= 0

def median(x, y, z):
    if x > y:
        temp = x
        x = y
        y = temp
    if z < x:
        return x
    if z < y:
        return z
    return y


assert median(3, 1, 2) == 2
