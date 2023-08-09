# ✔ Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# ✔ Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# ✔ Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


import json


class User:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level


    def __str__(self):
        return f'User id = {self.id}'


def json_to_users(file_name):
    with open(file_name, encoding='UTF-8') as f1:
        data = json.load(f1)
    users = set()
    for id in data:
        users.add(User(id=id, name=data[id][0], level=data[id][1]))
    return users


print(*json_to_users('res2.json'))
