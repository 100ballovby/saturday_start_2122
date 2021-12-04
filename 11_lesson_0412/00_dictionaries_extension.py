student = {
    'Miron': 3,
    'Zakhar': 9,
    'Andrew': 9,
    'Vlad': 7,
}

mid = 0
for mark in student.values():  # перебираю каждую оценку в словаре
    mid += mark  # складываю каждую оценку и получаю итоговую сумму

mid = mid / len(student)
print(mid)



