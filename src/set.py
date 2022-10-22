def check_characters(str1):
    chars = set(str1)
    return len(chars)

def check_dicsize(dic1):
    set_from_dic = set(dic1)
    return len(set_from_dic)

def count_words(str_engsentences):
    symbols = ['.', ',', ':', ';', '!', '?']
    str1 = str_engsentences
    for symbol in symbols:
        str1 = str1.replace(symbol, '')
    return len(set(str1.split(' ')))

def operation_sample():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(set1.intersection(set2)) # 論理積
    print(set1.union(set2)) # 論理和
    print(set1.difference(set2)) # 差集合
    print(set1.symmetric_difference(set2)) # 対称差

if __name__ == "__main__":
    operation_sample()