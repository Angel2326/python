# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
# метод.
from colorama import Fore, Back, Style
from time import sleep

def loop(x):
        x.running('красный', 7)
        x.running('желтый', 2)
        x.running('зеленый', 7)
class TrafficLight:
    def running(self,color,user_delay):
        self.__color = color
        print(my_dict[self.__color] +  self.__color  )
        sleep(user_delay)
TrafficLight_101 = TrafficLight()
my_dict = {'красный':Fore.RED, 'желтый': Fore.YELLOW, 'зеленый':Fore.GREEN}
loop(TrafficLight_101)
