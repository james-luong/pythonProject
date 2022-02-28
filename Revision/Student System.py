class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects.replace(" ", "").split(',')
        self.is_male = is_male
        self.enrolled = True

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.phone_number)
        print(self.form_class)
        print(self.subjects)
        if self.is_male:
            print('Male')
        else:
            print('Female')
        print(self.enrolled)


s1 = Student('Karen', 17, '123-4567', 'WNLR', '13DTC, 13 SMX', False)
Student.display_info(s1)