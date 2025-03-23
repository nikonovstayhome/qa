from eugene_mentor.homework2_from_eugene.models.human import Human


class Student(Human):
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}"

    def add_grades(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def get_grades(self):
        return grades
