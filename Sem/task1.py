# ✔ Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# ✔ Обрабатывайте не числовые данные как исключения.

def input_num():
    while True:
        try:
            num = float(input('Введите число: '))
            break
        except ValueError as e:
            print(e)
    return num


print(input_num())
