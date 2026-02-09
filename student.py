class Student:
    # Standard 4.0 scale mapping (letter → points)
    __GRADE_POINTS = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0,
        "F": 0.0
    }

    def __init__(self, student_id: str, name: str):
        self.__student_id = student_id
        self.__name = name
        self.__enrolled_courses = []    # list[Course] — current enrollments
        self.__grades = {}              # dict[Course, str] — historical letter grades (only when assigned)

    def get_student_id(self) -> str:
        return self.__student_id

    def get_name(self) -> str:
        return self.__name

    def get_grades(self) -> dict:
        return self.__grades.copy()  # safe copy

    def enroll_in_course(self, course) -> bool:
        """Called by Registrar after prereq check"""
        success = course.enroll_student(self)
        if success:
            self.__enrolled_courses.append(course)
        return success

    def drop_course(self, course) -> bool:
        if course in self.__enrolled_courses:
            course.drop_student(self)
            self.__enrolled_courses.remove(course)
            return True
        return False

    def receive_grade(self, course, grade: str):
        """Called only by Course.assign_grade()"""
        grade = grade.upper()
        if grade not in self.__GRADE_POINTS:
            raise ValueError(f"Invalid grade: {grade}")
        self.__grades[course] = grade

    def has_completed_course(self, course_code: str) -> bool:
        """For prerequisite checks — any recorded grade counts as completed"""
        return any(c.get_course_code() == course_code for c in self.__grades)

    def get_enrolled_courses(self) -> list[str]:
        return [course.get_course_code() for course in self.__enrolled_courses]

    def get_gpa(self) -> float:
        if not self.__grades:
            return 0.0
        total_points = 0.0
        total_credits = 0.0
        for course, grade in self.__grades.items():
            points = self.__GRADE_POINTS[grade]
            credits = course.get_credits()
            total_points += points * credits
            total_credits += credits
        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    def get_transcript(self) -> str:
        if not self.__grades:
            return f"Transcript for {self.__name} (ID: {self.__student_id}): No grades recorded yet."
        transcript = f"Transcript for {self.__name} (ID: {self.__student_id}):\n"
        for course, grade in self.__grades.items():
            transcript += f"{course.get_course_code()} - {course.get_title()}: {grade}\n"
        transcript += f"\nCumulative GPA: {self.get_gpa()}"
        return transcript