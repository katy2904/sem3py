#  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
#  последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Укажите количество элементов в списке: '))

from random import randint
lst = [randint(-10, 10) for i in range(n)]
print(lst)

lstresult =[]

for i in range((n + 1) // 2):
    lstresult.append(lst[i] * lst[-(i + 1)])

print(lstresult)