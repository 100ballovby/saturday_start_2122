string = 'Hi! I love python programming. And you?'


def lin_search(s, elem):
    if len(elem) < 1:
        for i in range(len(s)):  # количество повторений = длине строки
            if s[i] == elem:  # если искомое совпало с текущим значением
                break  # выйти из цикла
        return i  # вернуть индекс элемента
    else:
        return 'Must be only 1 symbol.'


print(lin_search(string, 'mm'))


