# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class in_data:
    def __init__(self,day_1,month_1,year_1):
        self.day_1 =  day_1
        self.month_1 = month_1
        self.year_1 = year_1

    @staticmethod
    def valid(num1,num2,num3):
        if num1 > num2 and num1 < num3:
            return print(f'Проверку прошло {num1:02}')
        else:
            print(f'Проверку не прошло {num1:02}')

    @classmethod
    def transform(cls, data):
        day_1,month_1,year_1 = map(int,data.split('-'))
        print (f'{day_1:02} {month_1:02} {year_1}')
        return in_data.valid(day_1,0,32), in_data.valid(month_1,0,13),in_data.valid(year_1,0,9999)

data_1 = in_data
data_1.transform("01-11-2020")


