# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем
# нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class division_by_null:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return (f"Нельзя делить на 0")

