import sys


def reverse_lookup(list1):
    dist = {};
    for value in list1:
        dist[value] = list1.index(value)
    return dist


def handle_collision(dic1, str1):
    dic2 = dic1.copy()
    n = len(str1)
    if dic2.get(n) is None:
        ls = [str1]
        dic2[n] = ls
    else:
        dic2[n].append(str1)
    return dic2


if __name__ == '__main__':
    dic1_orig = {3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
    dic1_result = {3: ['ham', 'egg', 'tea'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
    handle_collision(dic1_orig, 'tea')
    print(dic1_orig == dic1_result)
