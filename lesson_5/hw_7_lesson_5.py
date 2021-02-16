# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить
# прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать
# словарь с фирмами и их прибылями, а также
# словарь со средней прибылью. Если фирма получила
# убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

profit = {}
mid_prof = {}
prof = 0
prof_aver = 0
i = 0
with open('седьмое здание.txt', 'r', encoding="utf-8") as my_file:
    for line in my_file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
mid_prof = {'средняя прибыль': round(prof_aver)}
profit.update(mid_prof)
print(f'Прибыль каждой компании - {profit}')

with open('седьмое задание.json', 'w', encoding="utf-8") as js_file:
    json.dump(profit, js_file)
    js_str = json.dumps(profit)

print(f'Создан файл с расширением json со следующим содержимым: {js_str}')

