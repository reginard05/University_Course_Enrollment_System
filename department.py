class Department:
    def __init__(self, department_name: str):
        self.__department_name = department_name
        self.__courses = []                          # list[Course]
        self.__prerequisites_rules = {}              # dict[Course, list[str]] — prereq codes

    def get_name(self) -> str:
        return self.__department_name

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def get_department_courses(self) -> list:
        return self.__courses[:]

    def set_prerequisite(self, target_course, prerequisite_codes: list[str] | None = None):
        if target_course in self.__courses:
            self.__prerequisites_rules[target_course] = prerequisite_codes or []

    def check_prerequisite(self, student, target_course) -> bool:
        prereqs = self.__prerequisites_rules.get(target_course, [])
        for code in prereqs:
            if not student.has_completed_course(code):
                return False
        return True

    def find_course_by_keyword(self, keyword: str) -> str:
        matching = [c for c in self.__courses if keyword.lower() in c.get_title().lower()]
        if matching:
            return "\n".join([f"{c.get_course_code()}: {c.get_title()}" for c in matching])
        return "No courses found matching the keyword."