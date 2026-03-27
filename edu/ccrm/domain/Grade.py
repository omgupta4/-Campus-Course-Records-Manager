# edu/ccrm/domain/Grade.py

from enum import Enum


class Grade(Enum):
    A = 4.0
    B = 3.0
    C = 2.0
    D = 1.0
    F = 0.0

    @property
    def points(self):
        return self.value

    def __str__(self):
        return f"{self.name}({self.value})"