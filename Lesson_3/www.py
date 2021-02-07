user_str = input('Введите строку: ')
user_word = []
num = 1
for element in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f" {num} {user_word[element]}")
        num = num + 1
    else:
        print(f" {num} {user_word[element][0:10]}")
        num = num + 1
