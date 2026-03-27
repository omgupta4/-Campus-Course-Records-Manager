# edu/ccrm/domain/Course.py

class Course:
    def __init__(self, code, title, credits, instructor, semester, department):
        self._code = code
        self._title = title
        self._credits = credits
        self._instructor = instructor
        self._semester = semester
        self._department = department

    # Getters
    @property
    def code(self):
        return self._code

    @property
    def title(self):
        return self._title

    @property
    def credits(self):
        return self._credits

    @property
    def instructor(self):
        return self._instructor

    @property
    def semester(self):
        return self._semester

    @property
    def department(self):
        return self._department

    def __str__(self):
        return f"Course[{self._code} - {self._title}, Credits: {self._credits}, Semester: {self._semester}, Dept: {self._department}]"