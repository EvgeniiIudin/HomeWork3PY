# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decNum = int(input('Введите десятичное число: '))
binNum = ''
while decNum > 0:
    binNum = str(decNum % 2) + binNum
    decNum = decNum // 2
print(binNum)
