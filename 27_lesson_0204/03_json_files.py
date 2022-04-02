import json

with open('numbers.json') as json_file:
    my_list = json.load(json_file)  # load() выгружает данные из файла и преобразовывает их в объект
    print(type(my_list))  # содержимое преобразовалось в список
    print(my_list[0])  # достать элемент с индексом 0


