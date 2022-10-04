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

print(round(maximum - minimum, 3))

# решение 2

for i in range(0, len(lst)):
    lst[i] = int(str(lst[i]).split('.')[1])
    if lst[i] < 100:
        lst[i] *= 10

maximum = max(lst)
minimum = min(lst)

print((maximum - minimum) / 1000)

