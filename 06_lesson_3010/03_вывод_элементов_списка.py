students = [
    "Zakhar", "John",
    "Paul", "Alice",
]

# списки поддерживают индексацию
print(students[1])
# пользуясь системой индексов я могу выводить элементы списка через цикл
for i in range(len(students)):
    print(f'i = {i}, элемент: {students[i]}')

# я могу просматривать список НЕ через индексы
for i in students:
    print(f'i = {i}')
# перебор элементов списка

