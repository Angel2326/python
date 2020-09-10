my_list = {'Зима': (1, 2, 12),'Весна': (3, 4, 5), 'Лето': (6, 7, 8),'Осень': (9, 10, 11)}

user_month = int(input('Введите месяц от 1 до 12: '))
for key in my_list.keys():
    if user_month in my_list[key]:
        print(key)

