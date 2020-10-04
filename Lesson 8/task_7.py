# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
import math


class Complex:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(complex(self.x, self.y))

    def __add__(self, other):
        return complex((self.x+other.x),(self.y+other.y))
    def __mul__(self, other):
        return complex((self.x*other.x-self.y*other.y),(self.x*other.y+other.x*self.y))

complex_1 = Complex(4,5)
complex_2 = Complex(1,1)
print(f'Сумма комплексных чисел =  {complex_1+complex_2}')
print(f'Произведение комплексных чисел =  {complex_1*complex_2}')

