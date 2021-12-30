def countdown(n):
    print(n)
    if n <= 0:
        return None
    else:
        return countdown(n - 1)

countdown(7)
