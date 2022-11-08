import sys


def invert(x):
    return -x


def main():
    # 高階関数
    ls = [3, -8, 1, 0, 7, -5]
    print(sorted(ls, key=invert))
    # ラムダ式
    print(sorted(ls, key=lambda x: -x))


def max_value_key(d):
    return max(d, key=lambda k: d[k])


def map_sample():
    mp = [abs(x) for x in [3, -8, 1, 0, 7, -5]]
    print(mp)
    mp = [x for x in map(abs, [3, -8, 1, 0, 7, -5])]
    print(mp)


def abs1(x):
    print('abs called on', x)
    return abs(x)


def map_iter():
    it = map(abs1, [3, -8, 1, 0, 7, -5])
    next(it)
    next(it)


def lambda_sample():
    lst = list(map(lambda x: x + 1, map(abs, [3, -8, 1, 0, 7, -5])))
    print(lst)
    total = sum(map(lambda x: x + 1, map(abs, [3, -8, 1, 0, 7, -5])))
    print(total)


def max_abs(ln):
    return max(map(abs, ln))


def number_of_big_numbers(ln, n):
    itr = filter(lambda x: x > n, ln)
    mp = map(lambda x: 1, itr)
    return sum(1 for x in itr)


def number_of_long_lines(file, n):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(map(lambda x: 1, filter(lambda x: len(x) > n, f)))
        # return sum(map(lambda x: 1, filter(lambda x: len(x) > n, f.readlines())))


if __name__ == "__main__":
    print(number_of_long_lines('text/jugemu.txt', 30))
