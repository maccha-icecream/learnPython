from dataclasses import dataclass


@dataclass
class Student:
    name: str


@dataclass
class Teacher:
    name: str
    is_principal: bool


def print_address(user: Student | Teacher) -> str:
    match user:
        case Student():
            print(f'{user.name}さんへ')
        # case Teacher() if not user.is_principal:
        case Teacher(is_principal=True):
            print(f'{user.name}校長先生へ')
        # case Teacher() if user.is_principal:
        case Teacher():
            print(f'{user.name}先生へ')
        case _:
            raise ValueError('Unknown')


if __name__ == "__main__":
    student = Student('Alice')
    teacher = Teacher('Bob', False)
    principal = Teacher('Charlie', True)

    print_address(student)
    print_address(teacher)
    print_address(principal)
