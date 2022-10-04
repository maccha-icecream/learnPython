import sys
import matplotlib.pyplot as plt
from time import sleep


def plot_chars():
    word = 'loremipsum'
    height = [0] * 26
    for c in word:
        height[ord(c) - ord('a')] += 1
    left = list(range(26))
    labels = [chr(i + ord('a')) for i in range(26)]
    plt.bar(left, height, tick_label=labels)
    plt.show()


def reverse_lookup2(dic1):
    dic2 = {}
    for key, value in dic1.items():
        dic2[value] = key
    return dic2


def sum_n(x, y):
    sum = 0
    for i in range(x, y + 1):
        sum += i
    return sum


def construct_list(int_size):
    list1 = [0] * int_size
    for i in range(int_size):
        list1[i] = i
    return list1


def sum_lists(list1):
    grand_total = 0
    for i in list1:
        sub_total = 0
        for j in i:
            sub_total += j
        grand_total += sub_total
    return grand_total


def simple_match(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        j = 0
        while j < len(str2) and str1[i + j] == str2[j]:
            j += 1
        if j == len(str2):
            return i
    return -1


def count10_yeah():
    cnt = 0
    while True:
        print('Yeah!')
        sleep(1)
        cnt += 1
        if cnt == 10:
            break


def collect_engwords(str_engsentence):
    str_engsentence = str_engsentence.replace(',', '')
    str_engsentence = str_engsentence.replace('.', '')
    words = str_engsentence.split(' ')
    list1 = []
    for word in words:
        if len(word) <= 2:
            continue
        list1.append(word)
    return list1


def swap_lists(ln1, ln2):
    for i, value in enumerate(ln1):
        if i % 2 == 1:
            ln2[i], ln1[i] = ln1[i], ln2[i]
    # return as tuple
    return (ln1, ln2)


def count_capitalletters(str1):
    uppercase_cnt = 0
    for i in range(len(str1)):
        str2 = str1[i].upper()
        str3 = str1[i].lower()
        if str1[i] == str2 and str2 != str3:
            uppercase_cnt += 1
    return uppercase_cnt


def identify_codons(str_augc):
    list1 = []
    for i in range(0, len(str_augc), 3):
        list1.append(str_augc[i: i + 3])
    return list1


def add_commas(int1):
    list1 = list(str(int1))
    str1 = ''
    count = 1
    for i in range(len(list1) - 1, -1, -1):
        str1 = list1[i] + str1
        if count % 3 == 0 and i != 0:
            str1 = ',' + str1
        # print(i, str1)
        count += 1
    return str1


def sum_strings(list1):
    if len(list1) < 3:
        return ','.join(list1)
    str1 = ''
    for k in range(len(list1)):
        if k == len(list1) - 1:
            return str1 + str(list1[k])
        if k == len(list1) - 2:
            str1 += str(list1[k]) + ' and '
        else:
            str1 += str(list1[k]) + ', '
    return str1

# 登録されていない値が見つからなかった場合、
# len(str) ~ 10の間を２回ループしているので無駄
def handle_collision2(dic1, str1):
    strlen = len(str1)
    if dic1.get(strlen) is None:
        dic1[strlen] = str1
        return dic1

    found = False
    i = len(str1)

    while i <= 10:
        if (i in dic1.keys()) == False:
            dic1[i] = str1
            break;
        i += 1
        if found == False and i == 10:
            found = True
            i = 1
            continue
        print(i)
    return dic1

# 模範解答のほうがわかりやすいし無駄がない
# def handle_collision2(dic1, str1):
#     n = len(str1)
#     for i in range(n, 11):
#         if dic1.get(i) is None:
#             dic1[i] = str1
#             return
#     for i in range(1, n):
#         if dic1.get(i) is None:
#             dic1[i] = str1
#             return

def handle_collision3(list1):
    dic1 = {}
    tmp_key, pos = list1[0][0], 0
    for i in range(1, len(list1)):
        cur_key, cur_value = list1[i]
        if tmp_key == cur_key:
            dic1[tmp_key] = list1[pos][1]
            tmp_key = cur_key
        else:
            if dic1.get(cur_key) is None:
                dic1[cur_key] = cur_value
    if tmp_key == list1[0][0]:
        dic1[tmp_key] = list1[0][1]
    return dic1

# def handle_collision3(list1):
#     dic1 = {}
#     for i in range(len(list1)):
#         list2 = list1[i]
#         if dic1.get(list2[0]) is None:
#             dic1[list2[0]] = list2[1]
#     return dic1

if __name__ == "__main__":
    print(handle_collision3(
        [[4, 'Midsummer'], [3, 'Richard III'], [1, 'Othello'], [2, 'Tempest'], [3, 'King John'], [1, 'Lear']]))

    # 辞書どうしの比較は順不同
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 3, 'a': 1}
    print(dict1 == dict2)