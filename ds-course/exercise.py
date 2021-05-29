answer_key = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

student_answers = [
    ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
    ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
    ["C", "B", "A", "E", "D", "C", "E", "E", "A", "D"],
    ["A", "B", "D", "C", "C", "D", "E", "E", "A", "D"],
    ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
]

student_grades = []
for student_answer in student_answers:
    student_grade = []
    for i in range(len(student_answer)):
        if student_answer[i] is answer_key[i]:
            student_grade.append(1)
        else:
            student_grade.append(0)
    grade = sum(student_grade) / len(answer_key)
    print(grade)
    student_grades.append(student_grade)

print(*student_grades, sep="\n")

matriz = []
for i in range(len(student_answers)):
    lista = []
    for j in range(len(student_answers[i])):
        if student_answers[i][j] is answer_key[j]:
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)

print(*matriz, sep="\n")
