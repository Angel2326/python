# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, size=4, height=6):
        self.size = size
        self.height = height

    @abstractmethod
    def rate_material_coat(self):
        return self.size / 6.5 + 0.5

    @abstractmethod
    def rate_material_costume(self):
        return self.height * 2 + 0.3




class Coat_Costume(Dress):
    def rate_material_costume(self):
        return self.height * 2 + 0.3

    def rate_material_coat(self):
        return self.size / 6.5 + 0.5
    @property
    def sum(self):
        return self.rate_material_costume()+self.rate_material_coat()
Clothe = Coat_Costume()
print(f'расход материала на костюм : {Clothe.rate_material_costume()} м')
print(f'расход материала на пальто : {round(Clothe.rate_material_coat(),2)} м')
print(f'суммарный расход материала : {round(Clothe.sum,2)} м')