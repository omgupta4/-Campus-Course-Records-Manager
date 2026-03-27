# edu/ccrm/service/EnrollmentService.py

from edu.ccrm.domain.Enrollment import Enrollment
from edu.ccrm.config.app_config import AppConfig
from edu.ccrm.service.exceptions import DuplicateEnrollmentException
from edu.ccrm.service.exceptions import MaxCreditLimitExceededException

class EnrollmentService:
    def __init__(self):
        self._enrollments = []

    # Enroll student with rules
    def enroll_student(self, student, course, semester):

        # ✅ 1. Check duplicate enrollment
        for e in self._enrollments:
            if (e.student == student and
                e.course == course and
                e.semester == semester):
                raise DuplicateEnrollmentException(
                    f"Student {student.reg_no} is already enrolled in {course.code}"
                )

        # ✅ 2. Check credit limit
        total_credits = sum(
            e.course.credits
            for e in self._enrollments
            if e.student == student and e.semester == semester
        )

        max_credits = AppConfig.get_instance().max_credits

        if total_credits + course.credits > max_credits:
            raise MaxCreditLimitExceededException(
                f"Student {student.reg_no} exceeds max {max_credits} credits with course {course.code}"
            )

        # ✅ 3. Enroll student
        e = Enrollment(student, course, semester)
        self._enrollments.append(e)
        student.enroll_course(course)
        print("✅ Student enrolled successfully!")

    # Unenroll student
    def unenroll_student(self, student, course):
        self._enrollments = [
            e for e in self._enrollments
            if not (e.student == student and e.course == course)
        ]
        student.unenroll_course(course)
        print("✅ Student unenrolled successfully!")

    # Assign Grade
    def assign_grade(self, student, course, grade):
        for e in self._enrollments:
            if e.student == student and e.course == course:
                e.grade = grade
                print("✅ Grade assigned successfully!")
                return
    # Compute GPA
    def compute_gpa(self, student):
        total_points = 0
        total_credits = 0

        for e in self._enrollments:
            if e.student == student and e.grade is not None:
                total_points += e.grade.points * e.course.credits
                total_credits += e.course.credits

        return total_points / total_credits if total_credits > 0 else 0.0

    # Print Transcript
    def print_transcript(self, student):
        print(f"Transcript for {student.full_name}:")

        for e in self._enrollments:
            if e.student == student:
                print(e)

        gpa = self.compute_gpa(student)
        print(f"Overall GPA: {gpa:.2f}")