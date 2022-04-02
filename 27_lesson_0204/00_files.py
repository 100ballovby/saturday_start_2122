with open('pi_digits.txt') as file_obj:  # file_obj = open('pi_digits.txt')
    pi_string = ''
    for line in file_obj:
        pi_string += line.strip()  # убирает лишние пробелы (если они там есть)
    pi_string = float(pi_string)
    print(pi_string)

# print(file_obj.read()) <- ошибка, потому что файл в этом месте программу уже закрыт
