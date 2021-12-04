from string import punctuation


subjects = {}

n = 5
mid = 0
for subject in range(n):
    name = input('Название предмета: ')
    mark = int(input('Оценка: '))
    subjects[name] = mark
    mid += subjects[name]

mid = mid / len(subjects)
print(f'Средний балл: {mid}')
print(subjects)
