# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Укажите количество элементов в списке: '))

from random import uniform
lst = [round(uniform(0, 10), 3) for i in range(n)]
print(lst)

# решение 1 - примитивно, в лоб, самые простые действия
maximum = lst[0] % 1
minimum = lst[0] % 1

for i in range(1, len(lst)):
    if lst[i] % 1 > maximum:
        maximum = lst[i] % 1
    if lst[i] % 1 < minimum:
        minimum = lst[i] % 1

print(f'разница между максимальным и минимальным значением дробной части элементов: '
      f'{round(maximum - minimum, 3)}')

# решение 2 - заморочилась с преобразованиями чтобы разобраться как это работает))
#lst = [5.25, 9.755, 4.139, 0.862, 3.097] -использовала этот список для поиска ошибок преобразований

for i in range(0, len(lst)):
    lst[i] = str(lst[i]).split('.')[1]
    if len(lst[i]) == 1:
        lst[i] = int(lst[i]) * 100
    elif len(lst[i]) == 2:
        lst[i] = int(lst[i]) * 10
    else:
        lst[i] = int(lst[i])

maximum = max(lst)
minimum = min(lst)

print(f'разница между максимальным и минимальным значением дробной части элементов: '
     f'{(maximum - minimum) / 1000}')

