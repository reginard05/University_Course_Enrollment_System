class Registrar:
    def __init__(self):
        self.__students_by_id = {}      # dict[str, Student]
        self.__courses_by_code = {}     # dict[str, Course]
        self.__departments = []         # list[Department]

    def add_student(self, student):
        sid = student.get_student_id()
        if sid not in self.__students_by_id:
            self.__students_by_id[sid] = student
        else:
            raise ValueError(f"Student {student.get_name()} already exists.")

    def add_course(self, course):
        code = course.get_course_code()
        if code not in self.__courses_by_code:
            self.__courses_by_code[code] = course
        else:
            raise ValueError(f"Course {code} already exists.")

    def add_department(self, department):
        if department not in self.__departments:
            self.__departments.append(department)

    def find_department_for_course(self, course):
        for dept in self.__departments:
            if course in dept.get_department_courses():
                return dept
        return None

    def enroll_student_in_course(self, student_id: str, course_code: str):
        student = self.__students_by_id.get(student_id)
        course = self.__courses_by_code.get(course_code)
        if not student or not course:
            print("Student or course not found.")
            return False

        dept = self.find_department_for_course(course)
        if dept and not dept.check_prerequisite(student, course):
            print(f"Prerequisite not met for {course_code}")
            return False

        return student.enroll_in_course(course)

    def generate_transcript(self, student_id: str) -> str:
        student = self.__students_by_id.get(student_id)
        if student:
            return student.get_transcript()
        return "Student not found."

    def generate_roster(self, course_code: str) -> str:
        course = self.__courses_by_code.get(course_code)
        if course:
            return course.roster()
        return "Course not found."

    def get_all_students(self) -> dict:
        return self.__students_by_id.copy()