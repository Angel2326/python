# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

from math import exp, log1p


# проверка на действительное число
def verify_float_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# проверка на целое число
def verify_int_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


# возводим в степень вариант_1
def my_func_1(x, y):
    return round((exp(y * log1p(x - 1))), 3)


# возводим в степень вариант_2
def my_func_2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= 1 / x
    return round(res,3)


while True:
    a = input('Введите действительное положительное число "a", необходимое для возведения:')
    if verify_float_number(a):
        b = input('Введите степень "b" (целое отрицательное число): ')
        if verify_int_number(b) and int(b) < 0:
            print('a^b = ', my_func_1(float(a), int(b)))
            print('a^b = ', my_func_2(float(a), int(b)))
        else:
            print('Введите корректное число "b"')
    else:
        print('Введите корректное число "a"')
