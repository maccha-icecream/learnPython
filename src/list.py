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
    numbers = [10, 21, 86]
    number_with_prefix = [f'No.{x}' for x in numbers]
    print(number_with_prefix)