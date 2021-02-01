# 7. Реализовать генератор с помощью функции
# с ключевым словом yield, создающим очередное
# значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться
# следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле
# необходимо выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count
from math import factorial

num = int(input('Введите до какого числа вам нужен факториал: '))


def fact():
    for el in count(1):
        yield factorial(el)


fact = fact()
x = 0
for i in fact:
    if x < num:
        print(i)
        x += 1
    else:
        break
