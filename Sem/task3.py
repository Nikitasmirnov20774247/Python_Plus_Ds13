# ✔ Создайте класс с базовым исключением и дочерние классыисключения:
# * ошибка уровня,
# * ошибка доступа.


class UserException(Exception):
    pass


class LevelException(UserException):
    pass


class AccessException(UserException):
    pass
