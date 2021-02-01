# 1. Реализовать скрипт, в котором должна
# быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

name, hours, rate_per_hour, prize = argv

hours = int(hours)
rate_per_hour = int(rate_per_hour)
prize = int(prize)


def salary(arg1, arg2, arg3):
    salary = (arg1 * arg2) + arg3
    return salary


print(salary(hours, rate_per_hour, prize))
