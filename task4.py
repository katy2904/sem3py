# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101,  3 -> 11,  2 -> 10

number = int(input('Введите число для преобразования: '))
print(f'Десятичное число {number} равно двоичному', end=' ')

bistr = ''

while number >= 1:
    bistr += str(number - number // 2 * 2)
    number //= 2

binumber = int(bistr[::-1])

print(binumber)
