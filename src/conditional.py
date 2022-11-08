import sys


def exception3(x, y, z):
    if x == y:
        return z
    elif x == z:
        return y
    return x


def exception9(a):
    x = a[0]
    for y in a:
        if x != y:
            return y


if __name__ == '__main__':
    x = 15
    if 10 <= x <= 20:
        print(x)
