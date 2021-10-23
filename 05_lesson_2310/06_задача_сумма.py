"""Нужно написать программу, которая найдет
сумму всех чисел от 1 до 100 включительно"""

# вариант 1
summary = 0
for i in range(1, 101):
    summary += i
print(summary)

# вариант 2
summary = 0
i = 1
while i <= 100:
    summary += i
    i += 1
print(summary)

# вариант 3
print(sum(range(1, 101)))  # сумма диапазона от 1 до 100 включительно
# sum(collection) <- сумма элементов коллекции
