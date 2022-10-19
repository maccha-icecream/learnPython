import enum
from enum import Enum

@enum.unique
class BloodType(enum.IntEnum):
    A = 1
    B = 2
    O = 3
    AB = 4

    def __str__(self):
        return self.name

    @classmethod
    def show_all(cls) -> list[str]:
        return list(map(lambda c:c.value, cls))
