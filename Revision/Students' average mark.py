students_list = []
total_mark = 0
best_mark = 0

while True:
    name = input("Student's name: ").capitalize()

    if name == 'X':
        break

    else:
        mark = float(input("Student's mark: "))
        total_mark += mark

    students_list.append([name, mark])

for i in students_list:
    if i[1] >= best_mark:
        best_mark = i[1]

for student in students_list:
    if student[1] == best_mark:
        print(f'The best student is {student[0]} with {student[1]} points')

print(f'Average mark for all students is {total_mark/len(students_list)} points')