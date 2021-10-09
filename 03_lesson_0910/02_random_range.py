import random as r

num = r.randint(-100, 100)

if num in range(1, 101):
    print(num)
elif num == 0:
    print('0 нельзя!')
else:
    print(f'Число {num} меньше 0, меняю знак!')
    print(num * -1)


