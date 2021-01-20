#Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

#это способ решения без использования цикллов

data_type = [0, 'day', 153.2, 'night']
zerro = type(data_type[0])
first = type(data_type[1])
second = type(data_type[2])
therd = type(data_type[3])
print(zerro, first, second, therd)


#Это способ с использованием цикла for "" in ""

data_type = [0, 'day', 153.2, 'night']
for element in data_type:
    print(type(element))

#Это способ с запросом переменных у пользователя

data_type = []
count = int(input("Сколько значений вы желаете ввести?: "))
print("Сейчас вы будете вводить значения поочерёдно")
i = 0
while i < count:
    data_type.append(input("Введите значение"))
    i = i + 1
for element in data_type:
    print(type(element))

#Здесь всегда тип будет строчным так как я написал просто input.
#Мне бы хотелось узнать как можно поменять input чтобы он распознавал любые типы