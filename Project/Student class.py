class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_students = max_student
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            return total/len(self.students)

# Main routine

# instantiate 3 students objects
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Caleb", 19, 65)

# instantiate course object
course1 = Course("Computer Science", 2)

# add students to course
course1.add_students(s1)
course1.add_students(s2)
print(course1.add_students(s3))

print(f"The average grade in {course1.name} is {course1.get_average_grade()}")