# edu/ccrm/domain/Instructor.py

from edu.ccrm.domain.Person import Person


class Instructor(Person):
    def __init__(self, id, full_name, email, department):
        super().__init__(id, full_name, email)
        self._department = department

    # Getter & Setter
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    # Override methods
    def get_profile(self):
        return f"Instructor Profile: {super().__str__()}, Department: {self._department}"

    def __str__(self):
        return f"[Instructor] {self.get_profile()}"