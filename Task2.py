# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

couples = []

list = [randint(1, 10) for i in range(1, 11)]
print(list)

N = len(list)
for i in range(N//2):
    couples.append(list[i] * list[N-1])
print(couples)
