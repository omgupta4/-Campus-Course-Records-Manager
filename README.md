# Campus Course & Records Manager (CCRM)
## 📋 Project Overview:
A comprehensive console-based Python application for managing academic records, including students, courses, enrollments, and grading systems. 
Built with modern Python features, demonstrating Object-Oriented Programming (OOP) principles, design patterns, exception handling, file handling, and CLI workflows.

## 🎯 Key Features:
- **Student Management**: Complete CRUD operations for student records
- **Course Catalog**: Manage course offerings with credits and departments
- **Enrollment System**: Handle course registrations with validation rules
- **Grading & Transcripts**: Assign grades and generate academic transcripts
- **File Operations**: Import/export data in CSV format
- **Backup System**: Automated timestamped backups
- **Analytics**: GPA reports, top performers, and distribution analysis
- **Exception Handling**: Comprehensive error management

## 🏗️ Architecture:
- **Modular Design**: Separated into domain, service, and I/O layers
- **Object-Oriented**: Implements OOP principles and design patterns
- **Console Interface**: User-friendly CLI with color-coded menus
- **Configuration Management**: Singleton pattern for app settings

---

## 🚀 How to Run
### Prerequisites:
- **Python 3.8 or higher**
- **Command-line terminal** (PowerShell, Command Prompt, or Terminal)
- **Run The Application**:
  ```sh

  # Navigate to project folder
  cd Campus-Course-Record-Manager

  # Run main file
  python main.py

### 🧪 Sample Workflow:
1. Start the application from main menu
2. Add students through "Manage Students" → "Add Student"
3. Create courses via "Manage Courses" → "Add Course"
4. Enroll students in courses with automatic validation
5. Assign grades and generate transcripts
6. Export data or generate reports

---

## 🐍 Python Features Used:
- **OOP Concepts**: Classes, inheritance, polymorphism
- **Dataclasses**: Simplified model classes
- **Enums**: For grades and semesters
- **Exception Handling**: Custom exceptions
- **File Handling**: CSV read/write using `csv` module
- **Datetime**: Timestamp-based backups
- **List Comprehensions & Lambda**: Data filtering and sorting
- **Recursion**: Utility functions (e.g., directory size)

## 🧩 Python Equivalent Concepts (Syllabus → Code):

| Syllabus Topic                  | Where Implemented (File / Class / Method)                     |
|---------------------------------|----------------------------------------------------------------|
| **Encapsulation**                | All model classes (`Student.py`, `Course.py`) using private variables (`_var`) + `@property` getters/setters |
| **Inheritance**                  | `Person.py` (base class) → extended by `Student.py`, `Instructor.py` |
| **Abstraction**                  | `Person.py` using `abc.ABC` with abstract method `getRole()`) |
| **Polymorphism**                 | Overridden `getRole()`, `__str__()` in `Student.py` & `Instructor.py` |
| **Interfaces**                   | `StudentService.py`, `CourseService.py`,`EnrollmentService.py`,`ReportService.py` etc.             |
| **Singleton Pattern**            | `AppConfig.py` (ensures single instance for storing students & courses) |
| **Custom Exceptions**            | `DuplicateEnrollmentException.py`, `MaxCreditLimitExceededException.py` |
| **Exception Handling**           | `CampusApp.py` (try/catch in enrollment, import/export workflows)      |
| **Checked & Unchecked Exceptions** | Python uses only unchecked exceptions; custom exceptions raised in services and handled in CLI  |
| **Date/Time API**                | `datetime` module (`student.py` for admission_date, `backup.py` for timestamp folders) |
| **Enums**                        | `Grade.py` (stores points), `Semester.py` (SPRING, SUMMER, FALL, WINTER) |
| **List Comprehensions / Lambdas**            | `CourseService.py` (filtering by instructor/department), `CampusApp.gpaReportUI()` (GPA calculations) |
| **Recursion**                    | `recursion_utils.py`, `backup.py` (directory size calculation)    |
| **File I/O**             | `file_handler.py`, `backup.py` using `open()`, `csv`, `pathlib` |
| **Anonymous Functions**          | Lambda functions used for sorting (e.g., `sorted(students, key=lambda s: s.gpa)`)                 |
| **Assertions**                   | `Course.py` constructor (`assert credits > 0 && credits <= 18`) |
| **Arrays & Array Utilities**     | `courseservice.py`, sorting examples with `Arrays.sort()` |


---

## 🧪 Notes on Enabling Assertions:

Assertions are used in the project to enforce invariants.  
For example, in `Course.py` constructor:

```python
  assert credits > 0 && credits <= 18 : "Credits must be between 1 and 18";
```

## Design Patterns Used:
- **Singleton**: Config class for global settings
- **Service Layer**: Business logic separation
- **Factory Pattern**: Object creation patterns in service classes
- **DTO Pattern**: Data transfer using dictionaries

---

## 📁 Project Structure Deep Dive:
```text
Campus-Course-Record-Manager/
├── src/
│   ├── edu/ccrm/
│   │   ├── cli/           # Command-line interface
│   │   ├── config/        # Configuration management
│   │   ├── domain/        # Business entities
│   │   ├── io/           # File operations
│   │   └── service/      # Business logic
├── students.csv          # Sample student data
├── courses.csv          # Sample course catalog
└── README.md           # Project documentation
```

---

## 🔮 Future Enhancements:
Potential improvements for the project:

- Database integration with SQLite / PostgreSQL
- Web interface using Flask / Django
- REST API for external integrations
- Advanced reporting with graphs (Matplotlib / Pandas)
- User authentication system
- Batch processing for large datasets

---