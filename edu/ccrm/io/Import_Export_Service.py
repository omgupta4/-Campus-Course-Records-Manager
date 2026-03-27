# edu/ccrm/io/ImportExportService.py

import csv
import random
from edu.ccrm.domain.Student import Student
from edu.ccrm.domain.Course import Course
from edu.ccrm.domain.Semester import Semester

class ImportExportService:

    def __init__(self, student_service, course_service):
        self._student_service = student_service
        self._course_service = course_service

    # ✅ Export Students to CSV
    def export_students(self, file_path):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            for s in self._student_service.get_all_students():
                writer.writerow([
                    s.reg_no,
                    s.full_name,
                    s.email,
                    s.status
                ])

    # ✅ Import Students from CSV
    def import_students(self, file_path):
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)

            for parts in reader:
                if len(parts) >= 4:
                    s = Student(
                        random.randint(1, 1000),  # dummy ID
                        parts[1],
                        parts[2],
                        parts[0],
                        parts[3]
                    )
                    self._student_service.add_student(s)

    # ✅ Export Courses to CSV
    def export_courses(self, file_path):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            for c in self._course_service.get_all_courses():
                writer.writerow([
                    c.code,
                    c.title,
                    c.credits,
                    c.department
                ])

    # ✅ Import Courses from CSV
    def import_courses(self, file_path):
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)

            for parts in reader:
                if len(parts) >= 4:
                    c = Course(
                        parts[0],
                        parts[1],
                        int(parts[2]),
                        None,
                        Semester.SPRING,
                        parts[3]
                    )
                    self._course_service.add_course(c)