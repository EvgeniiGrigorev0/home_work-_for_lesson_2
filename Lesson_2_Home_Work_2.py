#2. Для списка реализовать обмен значений соседних элементов,
#т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().

count = int(input("Сколько значений вы желаете ввести?: "))
user_values = []
i = 0
element = 0
while i < count:
    user_values.append(input("Введите следующее значение списка "))
    i = i + 1

for elements in range(int(len(user_values)/2)):
        user_values[element], user_values[element + 1] = user_values [element + 1], user_values[element]
        element = element + 2
print(user_values)

