l = ['Mon', 'Tue', 'Wed', 'Thu', 'fri', 'sat', 'sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

sample_func = lambda word: word.capitalize()

def sample_func2(word):
    return word.lower()


odd = [x for x in range(1, 11) if x % 2 == 1]
# odd_between_5_and_10 = list(filter(lambda x:x > 4, odd))
odd_between_5_and_10 = [x for x in odd if x > 4]
print(odd_between_5_and_10)
square_of_odds = [x ** 2 for x in odd]
print(square_of_odds)
