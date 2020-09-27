# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        s = ''
        for row in self.matr:
            for x in row:
                s += "{:4d}".format(x)
            s += '\n'
        return s

    def __add__(self, other):
        B = max(len(self.matr[0]), len(other.matr[0])) #находим максимальное количество строк матриц
        A = max(len(self.matr), len(other.matr)) #находим максимальное количество столбцов матриц
        W_self, W_other = [[0 for j in range(B)] for i in range(A)], [[0 for j in range(B)] for i in range(A)] # формируем нулевые матрицы
        #заполняем нулевые матрицы
        for i in range(len(self.matr)):
            for j in range(len(self.matr[0])):
                W_self[i][j] = self.matr[i][j]
        for i in range(len(other.matr)):
            for j in range(len(other.matr[0])):
                W_other[i][j] = other.matr[i][j]
        #формируем матрицы одинаковой размерности
        self.matr, other.matr = W_self, W_other
       # print(self.matr)
       # print(other.matr)

        # складываем матрицы
        for i in range(A):
            for j in range(B):
                self.matr[i][j] += other.matr[i][j]
        return self.matr


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])


print(matrix_1)
print(matrix_2)
print(matrix_3)
print(Matrix(Matrix(matrix_1 + matrix_2) + matrix_3)) # Как можно оптимизировать 54-ю строку или 42-ую??? Смог только так.
