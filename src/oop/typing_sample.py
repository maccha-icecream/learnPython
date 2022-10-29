from typing import Union, Optional

def main():
    a: int
    a = "foobar"
    test_list: list = [1,2,3]
    test_dict: dict = {'aichi': 'nagoya'}
    test_list = 42
    test_dict = "Nagoya"
    # <= Python 3.9
    # test_union_type: Union[int, float] = 10
    # >= Python 3.10
    test_union_type: int | float = 10
    test_union_type = 3.14
    test_union_type = None

    # <= Python 3.9
    test_optional: Optional[int] = None
    test_optional = 10
    test_optional = None
    test_optional = 2.83

if __name__ == "__main__":
    main()