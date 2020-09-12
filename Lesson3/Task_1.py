def div_func(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print ('Ошибка. Деление на 0')
        return div_func(int(input('Введите число (делимое)')),int(input('Введите число (делитель)')))

print('Частное = ', div_func(int(input('Введите число (делимое)')),int(input('Введите число (делитель)'))))
