# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
# примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    worker_name = 'Петр'
    worker_surname = 'Иванов'
    worker_position = 'Аналитик'
    _worker_income = {"wage": 20000, "bonus": 5000}

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.worker_name} {self.worker_surname}')
    def get_total_income(self):
        print(f' Cуммарный доход: {sum(self._worker_income.values())}')

boy = Position()
print(f'{boy.worker_name} {boy.worker_surname} {boy.worker_position} {boy._worker_income}')
boy.get_full_name()
boy.get_total_income()