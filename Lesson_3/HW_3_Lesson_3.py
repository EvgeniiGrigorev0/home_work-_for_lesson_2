# 3. Реализовать функцию my_func(),
# которая принимает три позиционных
# аргумента, и возвращает сумму
# наибольших двух аргументов.
first_value = int(input('Введите ваше первое значение: '))
second_value = int(input('Введите ваше второе значение: '))
third_value = int(input('Введите ваше третье значение: '))


def sum_high_arg(first_value, second_value, third_value):
    if first_value >= third_value and second_value >= third_value:
        return first_value + second_value
    elif second_value < first_value < third_value:
        return first_value + third_value
    else:
        return second_value + third_value


print(sum_high_arg(first_value, second_value, third_value))

