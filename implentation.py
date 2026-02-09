from course import Course
from department import Department
from student import Student
from registrar import Registrar


# ====================== DEMO ======================
if __name__ == "__main__":
    registrar = Registrar()

    cs_dept = Department("Computer Science")
    registrar.add_department(cs_dept)

    cs101 = Course("CS101", "Intro to Programming", credits=3.0, maximum_capacity=2)
    cs201 = Course("CS201", "Data Structures", credits=3.0)
    cs_dept.add_course(cs101)
    cs_dept.add_course(cs201)
    cs_dept.set_prerequisite(cs201, ["CS101"])

    registrar.add_course(cs101)
    registrar.add_course(cs201)

    kosi = Student("STU001", "Kosi")
    alice = Student("STU002", "Alice")
    bob = Student("STU003", "Bob")

    registrar.add_student(kosi)
    registrar.add_student(alice)
    registrar.add_student(bob)

    # Enrollment & waitlist
    registrar.enroll_student_in_course("STU001", "CS101")
    registrar.enroll_student_in_course("STU002", "CS101")
    registrar.enroll_student_in_course("STU003", "CS101")  # waitlisted

    # Grades
    cs101.assign_grade(kosi, "A")
    cs101.assign_grade(alice, "B+")

    # Prerequisite test
    registrar.enroll_student_in_course("STU001", "CS201")  # allowed
    registrar.enroll_student_in_course("STU003", "CS201")  # blocked

    # Reports
    print("\n=== Transcript ===")
    print(registrar.generate_transcript("STU001"))

    print("\n=== Roster ===")
    print(registrar.generate_roster("CS101"))

    # Drop & promotion
    print("\n=== Drop & Promotion ===")
    alice.drop_course(cs101)

    print("\n=== Updated Roster ===")
    print(registrar.generate_roster("CS101"))
T