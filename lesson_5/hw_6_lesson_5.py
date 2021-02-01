# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно,
# чтобы для каждого предмета не обязательно были все
# типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


def nums(word):
    num = []
    for i in word.lstrip():
        if i.isdigit():
            num.append(i)
    return "".join(num)


def subjs(string):
    total = 0
    words = string.split()
    for word in words:
        if word[0].isdigit():
            total += int(nums(word))
    return total


magazine = dict()
with open("шестое задание.txt", "r", encoding="utf-8") as my_file:
    for string in my_file:
        total = subjs(string)
        magazine[(string.split()[0][:-1])] = total

print(magazine)

