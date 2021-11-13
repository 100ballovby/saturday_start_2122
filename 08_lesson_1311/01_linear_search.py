import random as r
ray = []
for i in range(50):
    ray.append(r.randint(1, 201))

ray.sort()
print(ray)

# алгоритм бинарного поиска
low = 0
high = len(ray) - 1
mid = (low + high) // 2
res = None
key = int(input('Введи число: '))

while ray[mid] != key and low <= high:
    if key > ray[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print('Элемент не найден!')
else:
    print(f'Нашел! ID={mid}')

