class Course:
    def __init__(self, course_code: str, title: str, credits: float = 3.0, maximum_capacity: int = 30):
        self.__course_code = course_code
        self.__title = title
        self.__credits = credits
        self.__maximum_capacity = maximum_capacity
        self.__enrolled_students = []   # list[Student]
        self.__waitlist = []            # list[Student]

    def get_course_code(self) -> str:
        return self.__course_code

    def get_title(self) -> str:
        return self.__title

    def get_credits(self) -> float:
        return self.__credits

    def get_seats_available(self) -> int:
        return self.__maximum_capacity - len(self.__enrolled_students)

    def is_full(self) -> bool:
        return len(self.__enrolled_students) >= self.__maximum_capacity

    def enroll_student(self, student) -> bool:
        if not self.is_full():
            self.__enrolled_students.append(student)
            print(f"{student.get_name()} enrolled in {self.__course_code}")
            return True
        else:
            self.__waitlist.append(student)
            print(f"{student.get_name()} added to waitlist for {self.__course_code}")
            return False

    def drop_student(self, student):
        if student in self.__enrolled_students:
            self.__enrolled_students.remove(student)
            print(f"{student.get_name()} dropped {self.__course_code}")
            if self.__waitlist:
                promoted = self.__waitlist.pop(0)
                self.__enrolled_students.append(promoted)
                print(f"{promoted.get_name()} promoted from waitlist to {self.__course_code}")
        elif student in self.__waitlist:
            self.__waitlist.remove(student)
            print(f"{student.get_name()} removed from waitlist for {self.__course_code}")

    def assign_grade(self, student, grade: str) -> bool:
        if student in self.__enrolled_students:
            student.receive_grade(self, grade)
            print(f"Grade {grade} assigned to {student.get_name()} in {self.__course_code}")
            return True
        print(f"Cannot assign grade — {student.get_name()} not enrolled in {self.__course_code}")
        return False

    def get_enrollment_count(self) -> int:
        return len(self.__enrolled_students)

    def roster(self) -> str:
        if not self.__enrolled_students:
            return f"Roster for {self.__title} ({self.__course_code}): No students enrolled."
        roster = f"Roster for {self.__title} ({self.__course_code}):\n"
        for student in self.__enrolled_students:
            roster += f"  ID: {student.get_student_id()} - {student.get_name()}\n"
        return roster