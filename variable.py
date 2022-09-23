import sys
import math

g = 9.8
a = 10

def force(m):
    return  g * m

def ft_to_cm(feet, inch):
    cm_per_feet = 30.48
    cm_per_inch = cm_per_feet / 12
    return feet * cm_per_feet + inch * cm_per_inch

def quadratic(a, b, c, x):
    return a * x ** 2 + b * x + c

# heronの公式により三角形の面積を返す
def heron(a, b, c): # a, b, cは三辺の長さ
    s = 0.5 * (a + b + c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def qe_disc(a, b, c):
    return b ** 2 - 4 * a * c

def qe_solution1(a, b, c):
    ans = (-b - math.sqrt(qe_disc(a, b, c))) / 2 * a
    return ans

def qe_solution2(a, b, c):
    ans = (-b + math.sqrt(qe_disc(a, b, c))) / 2 * a
    return ans

def foo():
    return a
def bar():
    a = 3
    return a

if __name__ == '__main__':
    print(foo())
    print(bar())
