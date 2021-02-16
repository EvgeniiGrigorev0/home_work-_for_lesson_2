# 3. Создайте собственный класс-исключение,
# который должен проверять содержимое списка
# на наличие только чисел. Проверить работу
# исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять
# список. Класс-исключение должен контролировать
# типы данных элементов списка.

class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                w_or_q = input(f'Попробовать снова? Нажмите W чтобы продолжть, либо Q чтобы выйти:  ')
                if w_or_q == 'w' or w_or_q == 'W':
                    print(try_except.my_input())
                elif w_or_q == 'q' or w_or_q == 'Q':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'



try_except = Error()
print(try_except.my_input())
