import sys

def bmax(a, b):
    if a > b:
        return a
    else:
        return b

def absolute(x):
    if x < 0:
        return -x
    return x

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

if __name__ == '__main__':
    if -1.1:
        print('True')
    else:
        print('False')