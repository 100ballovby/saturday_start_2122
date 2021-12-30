"""
Факториал числа n - это последовательность чисел от 1 до n включительно.
Обозначается факториал как n!
4! = 1 * 2 * 3 * 4 = 24
"""

def factorial_simple(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(6))
