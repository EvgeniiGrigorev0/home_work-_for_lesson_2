# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

user_word = input('введите ваше слово: ')

def int_func():
    return user_word.capitalize()

print(int_func())

# Продолжить работу над заданием.
# В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную
# ранее функцию int_func().

user_str = input('Введите слова через пробел: ').split()
user_words = []

def int_func():
    return user_word.capitalize()

for user_word in user_str:
    user_words.append(int_func())

print(user_words)








