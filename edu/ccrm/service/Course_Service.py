# edu/ccrm/service/CourseService.py

class CourseService:
    def __init__(self):
        # Key: course code
        self._courses = {}

    # Get all courses
    def get_all_courses(self):
        return self._courses.values()

    # Create
    def add_course(self, course):
        self._courses[course.code] = course

    # Read
    def get_course(self, code):
        return self._courses.get(code)

    # Delete
    def remove_course(self, code):
        if code in self._courses:
            del self._courses[code]

    # List all
    def list_courses(self):
        for course in self._courses.values():
            print(course)

    # Filter by Instructor
    def find_by_instructor(self, instructor):
        return [
            c for c in self._courses.values()
            if c.instructor == instructor
        ]

    # Filter by Department
    def find_by_department(self, dept):
        return [
            c for c in self._courses.values()
            if c.department.lower() == dept.lower()
        ]

    # Filter by Semester
    def find_by_semester(self, semester):
        return [
            c for c in self._courses.values()
            if c.semester == semester
        ]