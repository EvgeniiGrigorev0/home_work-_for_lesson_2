# 4. Программа принимает действительное положительное
# число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание
# необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.

#Первый вариант решения:

x = int(input('Введите положительное значение х: '))
y = int(input('Введите отризательное значение у: '))


def my_func(x, y):
    if x == 0:
        print('Учи математику')
    else:
        return x ** y


c = my_func(x, y)

print(c)

#Второй вариант решения:

x = int(input('Введите положительное значение х: '))
y = int(input('Введите отризательное значение у: '))



def my_func(x, y):
    global i, result
    if x == 0:
        print('Учи математику')
    else:
        i = 1
        result = 1
    while i <= abs(y):
        result *= x
        i += 1
    return 1 / result


c = my_func(x, y)

print(c)