import sys

def last_line(name):
    with open(name, 'r') as f:
        for line in f:
            pass
    return line

def but_first(ls):
    it = iter(ls)
    next(it)
    return it

if __name__ == "__main__":
    it = but_first([0, 2, 4, 6, 8])
    assert type(it) == type(iter([]))  # type(it) では it は消費されない
    assert list(it) == [2, 4, 6, 8]