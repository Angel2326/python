# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
from functools import reduce
import json
def func(lst):
    new_list = []
    for el in lst[2:]:
        new_list.append(el)
    return new_list # новый список готов

average_profit = 0
counter = 0
my_dict = {}
with open('text_7.txt', 'r', encoding='utf-8') as f: # открываем файл
    textlines = f.readlines() # считываем файл
    for line in textlines:
        my_list = list(line.split())  # убираем  пробелы
        my_dict[my_list[0]] = reduce(lambda x, y: int(x) - int(y),func(my_list))  # создаем словарь , предварительно находим прибыль

        if my_dict[my_list[0]] > 0:
            average_profit += int(my_dict[my_list[0]])
            counter +=1
    print([my_dict, {'average_profit' : average_profit/counter}])

# преобразуем в json и запишем
with open("text_7.json", "w", encoding='utf-8') as f:
    json.dump([my_dict, {'average_profit' : average_profit/counter}], f)
    json_str=json.dumps([my_dict, {'average_profit' : average_profit/counter}])
    print(type(json_str)) # проверяем, д.б. str

with open('text_77.json', 'r') as f: # открываем файл
    my_list = json.load(f)
    print(type(my_list)) # проверяем, д.б. list
