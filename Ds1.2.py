# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# * вывода на печать,
# * сравнения,
# * сложения,
# * *умножения матриц


# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.


from random import randint


class ValFormatMatrixError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f'!! Матрицы разных размеров невозможно сложить !!'
        elif self.operation == '*':
            return f'!! Данные матрицы невозможно перемножить !!'
        else:
            return f'!! Данная матрица не возможна !!'


class Matrix:
    '''
    Класс Matrix
    Данный класс создаёт экземпляр матрицы по полученному массиву, если переданный массив верен.
    '''


    def __init__(self, matrix):
        '''
        Метод __init__
        Инициализация аргументов, а также проверка
        на возможность существования матрицы.
        '''
        if len(set(map(len, matrix))) != 1:
            raise ValFormatMatrixError('!=')
        self.count_row = len(matrix)
        self.count_col = len(matrix[0])
        self.matrix = matrix


    def __add__(self, other):
        '''
        Метод __add__
        Переопределенный метод для поэлементного сложения матриц.
        Выполняет сложение двух экземпляров класса, если
        у двух слагаемых одинаковый размер (число столбцов и строк).
        '''
        if self.count_row != other.count_row or self.count_col != other.count_col:
            raise ValFormatMatrixError('+')
        new_matrix = []

        for x in range(self.count_row):
            row = []
            for y in range(self.count_col):
                row.append(self.matrix[x][y] + other.matrix[x][y])
            new_matrix.append(row)

        return Matrix(new_matrix)


    def __mul__(self, other):
        '''
        Метод __mul__
        Переопределенный метод для умножения матриц.
        Выполняет умножение двух экземпляров класса, если
        число столбцов в первом сомножителе равно числу строк во втором.
        '''
        if self.count_col != other.count_row:
            raise ValFormatMatrixError('*')
        new_matrix = []

        for x in range(self.count_row):
            row = []
            for y in range(other.count_col):
                res = 0
                for z in range(self.count_col):
                    res += self.matrix[x][z] * other.matrix[z][y]
                row.append(res)
            new_matrix.append(row)

        return Matrix(new_matrix)


    def __eq__(self, other):
        '''
        Метод __eq__
        Переопределённый метод для сравнения матриц.
        Матрицы могут быть равны когда равны их длины и каждый элемент.
        '''
        return self.matrix == other.matrix


    def __str__(self):
        '''
        Метод __str__
        Переопределенный метод для вывода матрицы.
        "Красивый" вывод экземпляра матрицы.
        '''
        s = ''
        for i in range(len(self.matrix)):
            s += str(self.matrix[i]) + '\n'

        return s


if __name__ == '__main__':
    matrix1 = Matrix([[randint(1, 9) for _ in range(3)] for _ in range(3)])
    matrix2 = Matrix([[randint(1, 9) for _ in range(4)] for _ in range(3)])
    matrix3 = Matrix([[2, 9, 8, 9, 1],
                      [8, 5, 2, 1, 4],
                      [7, 6, 7, 9, 3]])
    matrix4 = Matrix([[7, 2, 8],
                      [2, 7, 3],
                      [3, 6, 6],
                      [1, 9, 5],
                      [1, 9, 6]])
    matrix5 = Matrix([[2, 9, 8, 9, 1],
                      [8, 5, 2, 1, 4],
                      [7, 6, 7, 9, 3]])


    print('Результат формирования матриц:\n')
    print(f'matrix1:\n{matrix1}')
    print(f'matrix2:\n{matrix2}')
    print(f'matrix3:\n{matrix3}')
    print(f'matrix4:\n{matrix4}')
    print(f'matrix5:\n{matrix5}')
    print('Вывод результата сложения матриц:')
    print(f'matrix1 + matrix2 = \n{matrix1 + matrix2}')
    print('Вывод результата умножения матриц:')
    print(f'matrix3 * matrix4 = \n{matrix3 * matrix4}')
    print('Вывод результата сравнения матриц:')
    print(f'matrix3 == matrix4 | {matrix3 == matrix4}')
    print(f'matrix3 == matrix5 | {matrix3 == matrix5}')
    print('\nВывод документации:')
    print(Matrix.__doc__)
    print(Matrix.__init__.__doc__)
    print(Matrix.__add__.__doc__)
    print(Matrix.__mul__.__doc__)
    print(Matrix.__eq__.__doc__)
    print(Matrix.__str__.__doc__)
