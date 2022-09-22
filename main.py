import sys
import math

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

if __name__ == '__main__':
    print(qe_solution2(1, -2, 1))
    assert qe_disc(1, -2, 1) == 0
    assert qe_disc(1, -5, 6) == 1
    assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
    assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
    assert round(qe_solution1(1, -5, 6) - 2, 6) == 0
    assert round(qe_solution2(1, -5, 6) - 3, 6) == 0
