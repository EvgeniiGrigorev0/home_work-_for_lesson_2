#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

#Решение с помощью словаря

winter_1 = [12, 1, 2]
spring_1 = [3, 4, 5]
summer_1 = [6, 7, 8]
autumn_1 = [9, 10, 11]
time_of_the_year = dict(winter='winter_1', spring='spring_1', summer='summer_1', autumn='autumn_1')
user_month = int(input("Введите месяц цыфрой: "))
if user_month == winter_1[0] or user_month == winter_1[1] or user_month == winter_1[2]:
    print("Зима")
elif user_month == spring_1[0] or user_month == spring_1[1] or user_month == spring_1[2]:
    print("Весна")
elif user_month == summer_1[0] or user_month == summer_1[1] or user_month == summer_1[2]:
    print("Лето")
elif user_month == autumn_1[0] or user_month == autumn_1[1] or user_month == autumn_1[2]:
    print("Осень")

#Решение с помощью списка

monthes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
user_month = int(input("Введите месяц цыфрой: "))
if user_month == monthes[11] or user_month == monthes[0] or user_month == monthes[1]:
    print(seasons[0])
elif user_month == monthes[2] or user_month == monthes[3] or user_month == monthes[4]:
    print(seasons[1])
elif user_month == monthes[5] or user_month == monthes[6] or user_month == monthes[7]:
    print(seasons[2])
elif user_month == monthes[8] or user_month == monthes[9] or user_month == monthes[10]:
    print(seasons[3])
