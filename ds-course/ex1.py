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

for n, student_answer in enumerate(student_answers, 1):
    correct_ones = [ok for ok, answer in zip(answer_key, student_answer) if ok == answer]
    print(f'El estudiante {n} tiene la calificación de {len(correct_ones)} aciertos')