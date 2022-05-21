string = 'Hi! My name is Dave. How are you, dude?'


def search_special(s):
    indexes = []  # индексы знаков препинания в строке
    quantity = 0
    for i in range(len(s)):
        if s[i] in '!?,.""-:;':  # проверяю, не находится ли символ строки среди специальных символов
            indexes.append(i)
            quantity += 1
    return quantity, indexes


summ, index = search_special(string)
print(f'Количество знаков: {summ}')
print(f'Порядковые номера знаков: {index}')
