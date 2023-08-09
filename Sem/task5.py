# ✔ Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
#     * Загрузка данных (функция из задания 4)
#     * Вход в систему - требует указать имя и id пользователя. Для
#     проверки наличия пользователя в множестве используйте
#     магический метод проверки на равенство пользователей.
#     Если такого пользователя нет, вызывайте исключение
#     доступа. А если пользователь есть, получите его уровень из
#     множества пользователей.
#     * Добавление пользователя. Если уровень пользователя
#     меньше, чем ваш уровень, вызывайте исключение уровня
#     доступа.


import json


class UserException(Exception):
    pass


class LevelException(UserException):
    pass


class AccessException(UserException):
    pass


class User:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level


    def __str__(self):
        return f'User id = {self.id} name = {self.name}'
    

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
    

    def __hash__(self) -> int:
        return hash((self.id, self.name))


class Project:
    def __init__(self):
        try:
            self.users = self.json_to_users()
        except:
            print('No users error')
            self.users = set()


    def json_to_users(self, file_name = 'res2.json'):
        with open(file_name, encoding='UTF-8') as f1:
            data = json.load(f1)
        users = set()
        for id in data:
            users.add(User(id=id, name=data[id][0], level=data[id][1]))
        return users


    def enter(self, name, id):
        tmp = User(name=name, id=id, level=0)
        for user in self.users:
            if tmp == user:
                self.user = user
                break
        else:
            raise AccessException
        

    def add_user(self, name, id, level):
        if self.user.level > level:
            raise AccessException
        else:
            self.users.add(User(name=name, id=id, level=level))


p = Project()
print(*p.users)
p.enter('Иван', '5')
p.add_user('Петр', 10, 6)
p.add_user('Петр1', 10, 1)
print(*p.users)
