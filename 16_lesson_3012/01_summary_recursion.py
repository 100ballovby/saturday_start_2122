def summary(n):
    if n == 0:
        return 0  # сумма чисел от 0 до 0 = 0
    else:
        return n + summary(n - 1)  # 4 + 3 + 2 + 1

print(summary(3))
print(summary(4))
print(summary(10))
