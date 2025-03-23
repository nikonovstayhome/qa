from eugene_mentor.homework2_from_eugene.models.human import Human

class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def add_subject(self, subject):
        self.subject.append(subject)

teacher1 = Teacher("George", 21, 52)
print(teacher1.add_subject("Math"))

