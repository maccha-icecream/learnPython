import sys

greeting_global = 'Hello'
# print(type(greeting_global))

# def greeting():
#     global greeting_global
#     greeting_global = 'Bonjour'
#     print(greeting_global)

# def average(nums):
#     return sum(nums) / len(nums)
#
# def greeting(en, number, name):
#     print(en * number + ',' + name)

# def greeting(name, en = 'Hello'):
#     print(en + ',' + name)

# 引数をタプルとして受け取る
# def greeting(*args):
#     print(type(args))
#     print(args)

# 引数を辞書として受け取る
# def greeting(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# 位置引数, 初期値をもつ引数, 可変長引数, 辞書型引数の順に指定
def greeting(greet, en = 'Hello', *args, **kwargs):
    print(greet)
    print(en)
    print(args)
    print(kwargs)

# グローバル変数と同じ名前の関数
# 既存の変数と同じ名前の関数を定義すると、元の変数はその新たな関数を参照するものとして変更される
def greeting_global():
    print('This is the greeting_global function.')

def sum(x, y):
    return x * y

def is_palindrome(palindrome):
    # return "".join(reversed(list(palindrome))) == palindrome
    return palindrome[::-1] == palindrome


if __name__ == "__main__":
    print(is_palindrome("しなもんぱんもれもんぱんもなし"))
    print(is_palindrome("よるくるよ"))