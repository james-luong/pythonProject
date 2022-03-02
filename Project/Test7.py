class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teachers_list.append(self)

    def display_info(self):
        print('Teacher name:', self.name)
        print('Teaching class:', self.subject)
        print('\n***********************************\n')

teachers_list = []
Teacher('Baker', 'GRA')
Teacher('Barker', 'MAT')
Teacher('Graham', 'BIO')
Teacher('Morgan', 'DTC')
Teacher('Bell', 'PHY')
Teacher('Nimmo', 'ART')
Teacher('McNicol', 'ENG')

teacher_name = ''
class_code = input('class code: ').upper()

for teacher in teachers_list:
    for subject in teacher.subject:
        print(subject)

print(teacher_name)