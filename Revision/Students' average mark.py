students_list = []

def average(marks):
    total_mark = 0
    for mark in marks:
        total_mark += mark

    average_mark = total_mark / len(marks)
    return average_mark

def student(name, mark):

    student_list = []
    student_mark = []

    while mark != 'X':

        mark = input(mark).lower()

        if mark == 'x':
            continue

        else:
            student_mark.append(mark)

    student_average = average(student_mark)
    student_mark = sorted(student_mark)
    student_list.append(name, student_mark, student_average)

