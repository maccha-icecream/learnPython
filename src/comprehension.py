
def square1() -> list[int]:
    squares: list = []
    for x in range(6):
        squares.append(x ** 2)
    return squares

def square2() -> list[int]:
    squares:list[int] = [x ** 2 for x in range(6)]
    return squares

def count_len_in_list() -> list[int]:
    strings: list[str] = ['The', 'quick', 'brown']
    return [len(elem) for elem in strings]

def to_int_from_str_list() -> list[int]:
    str1: str = '123,45,-3'
    numbers: list[str] = str1.split(",")
    return [int(x) for x in numbers]

# 平均を求める
def average(lst: list[float]) -> float:
    return sum(lst) / len(lst)

# 分散を求める
def var(lst: list[float]) -> float:
    avg: float = average(lst)
    diff_from_avg: list[float] = [(x - avg) ** 2 for x in lst]
    return average(diff_from_avg)

def sum_lists(list1: list[list[int]]) -> int:
    return sum([sum(x) for x in list1])

def sum_matrix(list1: list[list[int]], list2: list[list[int]]) -> list[list[int]]:
    return [[list1[i][j] + list2[i][j] for j in range(3)] for i in range(3)]

def count_len_str_in_list() -> set[int]:
    words = ['cat', 'dog', 'elephant', None, 'giraffe']
    return {len(word) for word in words if word is not None}

def count_len_as_dict() -> dict[str, int]:
    words = ['cat', 'dog', 'elephant', None, 'giraffe']
    return {w: len(w) for w in words if w is not None}

def generator() -> None:
    it = (x * 3 for x in 'abc')
    for x in it:
        print(x)


if __name__ == "__main__":
   lst = list(x ** 2 for x in range(5))
   print(lst)
   tpl = tuple(x ** 2 for x in range(5))
   print(tpl)
   total = sum([x ** 2 for x in range(5)])
   print(total)
   total = sum(x ** 2 for x in range(5))
   print(total)
   anyMatch = any(x % 2 == 1 for x in range(5))
   print(anyMatch)
   allMatch = all(x % 2 == 1 for x in range(5))
   print(allMatch)