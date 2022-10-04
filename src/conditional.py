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
            return  y


if __name__ == '__main__':
    print(exception3(1, 2, 2))
    print(exception3(4, 2, 4))
    print(exception3(9, 3, 9))

    print(exception9([1, 2, 2, 2, 2, 2, 2, 2, 2]))
    print(exception9([4, 4, 4, 4, 4, 2, 4, 4, 4]))
    print(exception9([9, 9, 9, 9, 9, 9, 9, 9, 3]))

    x = -1
    if x < 1:
        print('x is less than 1')
    elif x < 2:
        print('x is larger than or equal to 1, and less than 2')
    elif x < 3:
        print('x is larger than or equal to 2, and less than 3')
    else:
        print('x is larger or equal to 3')