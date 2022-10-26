t = (1, 2, 3, 4, 5)

l = [x for x in t if x % 2 == 0]
print(l)

t2 = (5, 6, 7, 8, 9, 10)
l2 = [x * y for x in t for y in t2]
print(l2)

w = ['mon', 'tue', 'wed']
d = ['coffee', 'milk', 'water']

d = {x: y for x, y in zip(w, d)}
print(d)


s = {i for i in range(10) if i % 2 == 0}
print(s)


def g():
    for i in range(10):
        yield i


g = g()
g = (i for i in range(10) if i % 2 == 0)
print(type(g))
for x in g:
    print(x)