# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

...

name = input('Введите ваше имя: ')
surname = input('Введите фамилию: ')
date_of_birthday = input('Введите год вашего рождения: ')
city = input('Введите ваш город проживания')
email = input('Введите вашу электронную почту: ')
mobile_phone = input('Введите ваш теелфон: ')

...


def info_of_person(name, surname, date_of_birthday, city, email, mobile_phone):
    return ' '.join(
        [name, surname, date_of_birthday, city, email, mobile_phone])


print(info_of_person(name, surname, date_of_birthday, city, email, mobile_phone))

