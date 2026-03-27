# edu/ccrm/service/ReportService.py

class ReportService:
    def __init__(self, enrollment_service):
        self._enrollment_service = enrollment_service

    # ✅ 1. Top N Students by GPA
    def print_top_students(self, n, all_students):
        print(f"\n--- Top {n} Students by GPA ---")

        # Create list of (student, gpa)
        student_gpa = [
            (s, self._enrollment_service.compute_gpa(s))
            for s in all_students
            if self._enrollment_service.compute_gpa(s) > 0
        ]

        # Sort descending by GPA
        student_gpa.sort(key=lambda x: x[1], reverse=True)

        # Print top N
        for s, gpa in student_gpa[:n]:
            print(f"{s.full_name} (RegNo: {s.reg_no}) -> GPA: {gpa:.2f}")

    # ✅ 2. GPA Distribution (Histogram)
    def print_gpa_distribution(self, all_students):
        print("\n--- GPA Distribution ---")

        distribution = {}

        for s in all_students:
            gpa = self._enrollment_service.compute_gpa(s)

            if gpa >= 3.5:
                key = "3.5 - 4.0"
            elif gpa >= 3.0:
                key = "3.0 - 3.49"
            elif gpa >= 2.0:
                key = "2.0 - 2.99"
            elif gpa > 0:
                key = "< 2.0"
            else:
                key = "No GPA"

            distribution[key] = distribution.get(key, 0) + 1

        for range_key, count in distribution.items():
            print(f"{range_key} : {count} students")

    # ✅ 3. Average GPA Across All Students
    def print_average_gpa(self, all_students):
        gpas = [
            self._enrollment_service.compute_gpa(s)
            for s in all_students
            if self._enrollment_service.compute_gpa(s) > 0
        ]

        avg = sum(gpas) / len(gpas) if gpas else 0.0

        print(f"\n--- Average GPA of All Students: {avg:.2f} ---")