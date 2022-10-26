l = [1, 2, 3]
i = 5

# try~except
try:
    print(l[0])
except IndexError as e:
    print(f"Don't worry. :{e}")
except NameError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('done')
finally:
    print('clean up')


# 独自例外を定義
class UpperCaseError(Exception):
    pass

def check():
    words = ['APPLE', 'Orange', 'Banana']
    for word in words:
        if word.isupper():
            raise UpperCaseError(word)

try:
    check()
except UpperCaseError as e:
    print('This is my fault. Go next')