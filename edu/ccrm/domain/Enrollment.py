# edu/ccrm/domain/Enrollment.py

from datetime import date


class Enrollment:
    def __init__(self, student, course, semester):
        self._student = student
        self._course = course
        self._grade = None
        self._semester = semester
        self._enrollment_date = date.today()

    # Getters & Setters
    @property
    def student(self):
        return self._student

    @property
    def course(self):
        return self._course

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    @property
    def semester(self):
        return self._semester

    @property
    def enrollment_date(self):
        return self._enrollment_date

    def __str__(self):
        return (
            f"Enrollment[Student={self._student.reg_no}, "
            f"Course={self._course.code}, "
            f"Grade={self._grade}, "
            f"Semester={self._semester}]"
        )