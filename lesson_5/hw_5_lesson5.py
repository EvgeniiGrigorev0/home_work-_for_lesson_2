# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле
# и выводить ее на экран.

def summary():
    try:
        with open('пятое задание.txt', 'w+', encoding="utf-8") as my_file:
            line = input('Введите цифры через пробел: \n')
            my_file.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Вы ввели не число')


summary()
