# edu/ccrm/domain/Semester.py

from enum import Enum


class Semester(Enum):
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    FALL = "FALL"

    def __str__(self):
        # Convert "SPRING" → "Spring"
        return self.value.capitalize()