# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру,
# например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать
# в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class StoreMachines:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за ед: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'Что вы выбрали?: ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMachines.reception(self)


class Printer(StoreMachines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMachines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMachines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'
