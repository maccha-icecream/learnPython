import sys

def main():
    print("x")

def remove_evenindex(ln):
    return ln[1::2]

def change_domain(email, domain):
    address = email.split('@')
    address[len(address) - 1] = domain
    return '@'.join(address)

def reverse_totuple(ln):
    list_ln = list(ln)
    list_ln.sort(reverse=True)
    return tuple(list_ln)

def sum_list(ln):
    return sum(ln)

def atgc_countlist(str_atgc):
    list_count = []
    for bp in 'ATGC':
        int_bpcount = str_atgc.count(bp)
        list_count.append([int_bpcount, bp])
    return list_count

def square(ln):
    square1 = []
    for x in ln:
        square1.append(x ** 2)
    return square1

def square2(ln):
    return [x ** 2 for x in ln]

if __name__ == "__main__":
    print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')
    print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))

    print(sum_list([10, 20, 30]) == 60)
    print(sum_list([-1, 2, -3, 4, -5]) == -3)

    print(sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))

    original = [0, 1, 2, 3, 4, 5]
    print(square(original) == square2(original))

    a = []
    b = []
    b.append([1])
    d = [b, b]
    print(d[0] is d[1])
    b.append(1)
    print(d[0] is d[1])