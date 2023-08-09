# ✔ Создайте класс прямоугольник.
# ✔ Класс должен принимать длину и ширину при создании
# экземпляра.
# ✔ У класса должно быть два метода, возвращающие периметр
# и площадь.
# ✔ Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например:
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.


import math


class ArgumentNotFound(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"!! Аргумент не найден ({self.value}) !!"


class TypeValError(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"!! Значение не является числом ({self.value if self.value is not None else ''}) !!"


class NonPositiveError(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"!! Значение не может быть отрицательным ({self.value if self.value is not None else ''}) !!"


class NotZeroError(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"!! Значение не может быть равным 0 ({self.value if self.value is not None else ''}) !!"


class Rectangle:
    def __init__(self, a, b=None):
        self.is_valid(a, b)
        self.a = a
        self.b = a if not b else b


    def get_lenght(self):
        return 2 * (self.a + self.b)


    def get_area(self):
        return self.a * self.b
    

    @staticmethod
    def is_valid(a, b):
        if a is None:
            raise ArgumentNotFound(f"{a = }")
        if ((type(a) is not float) and (type(a) is not int)) or (b is not None and ((type(b) is not float) and (type(b) is not int))):
            raise TypeValError(f"{f'{a = }' if ((type(a) is not float) and (type(a) is not int)) else f'{b = }'}")
        if (a is not None and a < 0) or (b is not None and b < 0):
            raise NonPositiveError(f"{f'{a = }' if a < 0 else f'{b = }'}")
        if (a is not None and a == 0) or (b is not None and b == 0):
            raise NotZeroError(f"{f'{a = }' if a == 0 else f'{b = }'}")


r1 = Rectangle(-10, None)
print(r1.get_lenght())
print(r1.get_area())
