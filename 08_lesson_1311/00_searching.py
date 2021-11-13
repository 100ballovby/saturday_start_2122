import random as r

ray = []

for i in range(15):
    ray.append(r.randint(1, 99))

print(ray)
res = None
key = int(input('Что ищем? '))

for index in range(len(ray)):  # 0....len(ray)
    if key == ray[index]:  # если число найдено
        res = index
        break  # остановить поиск

if res is not None:
    print(f'Нашел! ID={res}.')
else:
    print('Элемент не найден!')


