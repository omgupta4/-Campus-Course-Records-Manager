# edu/ccrm/domain/Student.py
from datetime import date
from edu.ccrm.domain.Person import Person


class Student(Person):
    def __init__(self, id, full_name, email, reg_no, status):
        super().__init__(id, full_name, email)
        self._reg_no = reg_no
        self._status = status  # active/inactive
        self._date_joined = date.today()
        self._enrolled_courses = []

    # Getters & Setters
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def date_joined(self):
        return self._date_joined

    @property
    def enrolled_courses(self):
        return self._enrolled_courses

    # Methods
    def enroll_course(self, course):
        self._enrolled_courses.append(course)

    def unenroll_course(self, course):
        if course in self._enrolled_courses:
            self._enrolled_courses.remove(course)

    # Override methods
    def get_profile(self):
        return f"Student Profile: {super().__str__()}, RegNo: {self._reg_no}, Status: {self._status}"

    def __str__(self):
        return f"[Student] {self.get_profile()}"