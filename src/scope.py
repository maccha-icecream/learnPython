""""
TEST TEST ####
"""
animal = 'cat'


def f():
    """ TEST Func Doc """
    print(f.__name__)
    print(f.__doc__)

f()
print(__name__)
print('global:', globals())