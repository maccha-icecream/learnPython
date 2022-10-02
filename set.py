def main():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    print((s1 & s2))  # and
    print(s1 | s2)  # or
    print(s1 ^ s2)  # xor
    print(s1 - s2)  # diff
    print(s1.union(s2))  # union
    print(s1.intersection(s2))  # and(Intersection)
    print(s1.difference(s2))  # diff
    intersection = s1.intersection(s2)
    print((s1.union(s2)) - intersection)

if __name__ == "__main__":
    main()