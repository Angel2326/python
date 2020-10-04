# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
# данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_error(Exception):
    def __init__(self, txt):
        self.txt = txt

in_data = input('Введите выражение вида x/y:   ')
try:
    x, y = map(int, in_data.split('/'))
    if y == 0:
        raise My_error('Деление на 0 запрещено')
except (ValueError, My_error) as err:
    print(err)
else:
    print(round(x / y, 2))
