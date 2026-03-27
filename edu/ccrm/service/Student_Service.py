# edu/ccrm/service/StudentService.py

class StudentService:
    def __init__(self):
        # Key: reg_no
        self._students = {}

    # Get all students
    def get_all_students(self):
        return self._students.values()

    # Create
    def add_student(self, student):
        self._students[student.reg_no] = student

    # Read
    def get_student(self, reg_no):
        return self._students.get(reg_no)

    # Update
    def update_status(self, reg_no, status):
        s = self._students.get(reg_no)
        if s:
            s.status = status

    # Delete/Deactivate
    def deactivate_student(self, reg_no):
        s = self._students.get(reg_no)
        if s:
            s.status = "inactive"

    # List all
    def list_students(self):
        for student in self._students.values():
            print(student)

    # Print profile
    def print_profile(self, reg_no):
        s = self._students.get(reg_no)
        if s:
            print(s.get_profile())
        else:
            print("Student not found.")