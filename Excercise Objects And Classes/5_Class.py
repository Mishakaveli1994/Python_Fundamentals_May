class Class:
    __students_count = 22

    def __init__(self, class_name):
        self.name = class_name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > 0:
            Class.__students_count -= 1
            self.students.append(name)
            self.grades.append(float(grade))

    def get_average_grade(self):
        return float(f"{sum(self.grades) / len(self.grades):.2f}")

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
