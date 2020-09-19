# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

count = 0
sum = 0
print('Список сотрудников, ущемленные зарплатой: ')
with open('text_3.txt', encoding='utf-8') as f:  # открытие в режиме чтения
    for line in f:
        line_str = line.split()
        if float(line_str[1]) < 20000:
            print(line_str[0])
        count += 1
        sum += float(line_str[1])
print(f'Средний доход сотрудников: {sum / count:.8}')
