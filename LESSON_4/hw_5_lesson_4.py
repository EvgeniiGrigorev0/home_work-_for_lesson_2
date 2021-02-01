# 5. Реализовать формирование списка,
# используя функцию range() и возможности
# генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def result_func(el_1, el):
    return el_1 * el


print(f'Список чётных чисел от 100 до 1000: {my_list}')
print(f'Произведение всех елементов списка: {reduce(result_func, my_list)}')