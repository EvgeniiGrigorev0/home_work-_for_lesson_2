# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
#
# 1

from itertools import count

for el in count(int(input('Введите число с которого начать генерацию чисел: '))):
    print(el)

# 2

from itertools import cycle

my_lst = [1, 2, 3, 4, 'пять']

for el in cycle(my_lst):
    print(el)
