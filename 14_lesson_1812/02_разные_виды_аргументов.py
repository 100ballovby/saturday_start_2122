def power(n, p=2):
    """Возводит n в степень p"""
    res = 1
    for i in range(p):
        res *= n
    return res

print(power(2, 9))
# поименные аргументы
print(power(p=9, n=2))
# аргументы по умолчанию
print(power(5, 3))
print(power(8, 7))
print(power(10))

