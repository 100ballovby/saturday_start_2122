import random as r
n = int(input('Введи число: '))
r_list = []

# for i in range(n):  <- нам не подходит, потому что повторяется определенное количество раз
while len(r_list) < n:  # пока длина списка меньше нужной
    integer = r.randint(-100, 100)  # генерировать число
    if integer % 2 == 0:  # проверять, делится ли оно на 2 без остатка
        r_list.append(integer)  # и, если да, то добавлять в список

print(r_list)

