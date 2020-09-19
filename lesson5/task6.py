# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
from functools import reduce

# создаем список с часами для одного предмета
def func(lst):
    new_list = []
    for el in lst[1:]: #исключаем первый элемент
        if lst.index(el) != 0: # если прочерк, заменяем на 0
            if el =='-':
                el = 0
            else:
                el = el[:el.find('(')] # в противном случае получаем число, отсекая все лишнее
            new_list.append(el)
    return new_list # новый список готов


my_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f: # открываем файл
    textlines = list(f.readlines()) # считываем файл
    for line in textlines:
        my_list = list(line.replace(':','').split())  # убираем : после названия предмета, а также пробелы
        my_dict[my_list[0]] = int(reduce(lambda x,y: int(x) + int(y), func(my_list))) # создаем словарь , предварительно суммируя последовательность
    print(my_dict)



