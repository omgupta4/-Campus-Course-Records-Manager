# edu/ccrm/cli/Main.py

from edu.ccrm.domain.Student import Student
from edu.ccrm.domain.Course import Course
from edu.ccrm.domain.Grade import Grade
from edu.ccrm.domain.Semester import Semester
# from edu.ccrm.service import StudentService, CourseService,  EnrollmentService, ReportService
from edu.ccrm.service.Student_Service import StudentService
from edu.ccrm.service.Course_Service import CourseService
from edu.ccrm.service.Enrollment_Service import EnrollmentService
from edu.ccrm.service.Report_Service import ReportService

from edu.ccrm.io.Import_Export_Service import ImportExportService
from edu.ccrm.io.Backup_Service import BackupService
# from edu.ccrm.io import ImportExportService, BackupService

# Initialize services
student_service = StudentService()
course_service = CourseService()
enrollment_service = EnrollmentService()
report_service = ReportService(enrollment_service)

io_service = ImportExportService(student_service, course_service)
backup_service = BackupService()


# ANSI Colors
RESET  = "\033[0m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
RED    = "\033[31m"


# 🎨 Banner
def banner():
    print(CYAN +
          "=============================================\n"
          "   Welcome to Campus Course & Records Manager \n"
          "=============================================" +
          RESET)


# Main Menu
def print_main_menu():
    print(BLUE + "\n--- MAIN MENU ---" + RESET)
    print("1. Manage Students")
    print("2. Manage Courses")
    print("3. Enrollment & Grading")
    print("4. File Operations (Import/Export/Backup)")
    print("5. Reports & Analytics")
    print("6. Exit")


# ✅ Student Menu
def student_menu():
    print(BLUE + "\n--- STUDENT MANAGEMENT ---" + RESET)
    print("1. Add Student")
    print("2. List Students")
    print("3. Update Status")
    print("4. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        id = int(input("Enter ID: "))
        name = input("Full Name: ")
        email = input("Email: ")
        reg_no = input("RegNo: ")

        s = Student(id, name, email, reg_no, "active")
        student_service.add_student(s)

        print(GREEN + "✅ Student added successfully!" + RESET)

    elif choice == "2":
        student_service.list_students()

    elif choice == "3":
        reg_no = input("Enter RegNo: ")
        status = input("New Status (active/inactive): ")
        student_service.update_status(reg_no, status)

        print(GREEN + "✅ Status updated!" + RESET)


# ✅ Course Menu
def course_menu():
    print(BLUE + "\n--- COURSE MANAGEMENT ---" + RESET)
    print("1. Add Course")
    print("2. List Courses")
    print("3. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        code = input("Course Code: ")
        title = input("Title: ")
        credits = int(input("Credits: "))
        dept = input("Department: ")

        c = Course(code, title, credits, None, Semester.SPRING, dept)
        course_service.add_course(c)

        print(GREEN + "✅ Course added!" + RESET)

    elif choice == "2":
        course_service.list_courses()


# ✅ Enrollment Menu
def enrollment_menu():
    print(BLUE + "\n--- ENROLLMENT MANAGEMENT ---" + RESET)
    print("1. Enroll Student")
    print("2. Assign Grade")
    print("3. Print Transcript")
    print("4. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        reg_no = input("Enter RegNo: ")
        code = input("Enter Course Code: ")

        s = student_service.get_student(reg_no)
        c = course_service.get_course(code)

        if s and c:
            try:
                enrollment_service.enroll_student(s, c, Semester.SPRING)
                print(GREEN + "✅ Student enrolled!" + RESET)
            except Exception as e:
                print(RED + f"⚠ {e}" + RESET)
        else:
            print(RED + "⚠ Student or Course not found." + RESET)

    elif choice == "2":
        reg_no = input("RegNo: ")
        code = input("Course Code: ")
        grade_input = input("Grade (A/B/C/D/F): ").upper()

        try:
            grade = Grade[grade_input]
            enrollment_service.assign_grade(
                student_service.get_student(reg_no),
                course_service.get_course(code),
                grade
            )
            print(GREEN + "✅ Grade recorded!" + RESET)
        except:
            print(RED + "⚠ Invalid grade input!" + RESET)

    elif choice == "3":
        reg_no = input("Enter RegNo: ")
        s = student_service.get_student(reg_no)

        if s:
            enrollment_service.print_transcript(s)
        else:
            print(RED + "⚠ Student not found." + RESET)


# ✅ File Menu
def file_menu():
    print(BLUE + "\n--- FILE OPERATIONS ---" + RESET)
    print("1. Export Students to CSV")
    print("2. Import Students from CSV")
    print("3. Export Courses to CSV")
    print("4. Import Courses from CSV")
    print("5. Backup Data")
    print("6. Back")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            io_service.export_students("students.csv")
            print(GREEN + "✅ Students exported!" + RESET)

        elif choice == "2":
            io_service.import_students("students.csv")
            print(GREEN + "✅ Students imported!" + RESET)

        elif choice == "3":
            io_service.export_courses("courses.csv")
            print(GREEN + "✅ Courses exported!" + RESET)

        elif choice == "4":
            io_service.import_courses("courses.csv")
            print(GREEN + "✅ Courses imported!" + RESET)

        elif choice == "5":
            backup_service.backup(".", "backup")
            print(GREEN + "✅ Backup created successfully!" + RESET)

    except Exception as e:
        print(RED + f"⚠ Error: {e}" + RESET)


# ✅ Reports Menu
def reports_menu():
    print(BLUE + "\n--- REPORTS & ANALYTICS ---" + RESET)
    print("1. Top N Students by GPA")
    print("2. GPA Distribution")
    print("3. Average GPA")
    print("4. Back")

    choice = input("Enter choice: ")

    if choice == "1":
        n = int(input("Enter N: "))
        report_service.print_top_students(n, student_service.get_all_students())

    elif choice == "2":
        report_service.print_gpa_distribution(student_service.get_all_students())

    elif choice == "3":
        report_service.print_average_gpa(student_service.get_all_students())


# 🚀 Main
def main():
    banner()

    running = True
    while running:
        print_main_menu()
        choice = input(YELLOW + "Choose option: " + RESET)

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            enrollment_menu()
        elif choice == "4":
            file_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            print(GREEN + "Exiting... 🚀" + RESET)
            running = False
        else:
            print(RED + "Invalid choice!" + RESET)


if __name__ == "__main__":
    main()