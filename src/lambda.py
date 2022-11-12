def add_def(a, b = 1):
    return a + b


add_lambda = lambda a, b = 1: a + b


print(add_def(3, 4) == add_lambda(3, 4))
print(add_def(3) == add_lambda(3))


get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(3))
print(get_odd_even(4))

l = ('Charle', 'Bob', 'Alice')
# アルファベット順
l_sorted = sorted(l)
print(l_sorted)
# 2文字目のアルファベット順
l_sorted_len = sorted(l, key=lambda x: x[1])
print(l_sorted_len)


n = tuple(x for x in range(4))
# ラムダ式
# square = map(lambda x: x ** 2, n)
# print(tuple(square))
# リスト内包表記
square = (x ** 2 for x in n)
print(tuple(square))

# ラムダ式
# filter_even = filter(lambda x: x % 2 == 0, n)
# リスト内包表記
filter_even = tuple(x for x in n if x % 2 == 0)
print(tuple(filter_even))
