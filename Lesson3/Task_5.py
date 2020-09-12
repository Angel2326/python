# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def verify_float_number(str_1):
    try:
        float(str_1)
        return True
    except ValueError:
        return False


def s_func():
    while True:
        sum = 0
        global sum_1
        print('для выхода нажмите спец символ "q"')
        a = input('Введите cтроку чисел, разделенных пробелом\n')
        str_ = a.split()
        for el in str_:
            if verify_float_number(el):
                sum += float(el)
            elif not verify_float_number(el) and el.lower() == 'q':
                break
            else:
                print('Введено некоретное значение:', el)
        sum_1 += sum
        print('сумма данной строки: ', sum, 'сумма итоговая: ', sum_1)
        if not verify_float_number(el) and el.lower() == 'q':
            break


sum_1 = 0
s_func()
