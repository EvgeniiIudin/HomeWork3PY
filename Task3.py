# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

import random
maxNumb = 0
minNumb = 1

list = [round(random.uniform(1.0, 10.0), 3) for i in range(1, 6)] 
print("Массив дробных чисел: ")
print(list)

fract = [round(list[i]%1, 3) for i in range(len(list))]
print("Массив дробных частей чисел: ")
print(fract)

for item in fract:
    if (item > maxNumb): maxNumb = item
    if (item < minNumb): minNumb = item
print("Максимальное значение дробной части: ", maxNumb)
print("Минимальное значение дробной части: ", minNumb)
print("Разница между максимальным и минимальным значением дробной части элементов = ", maxNumb - minNumb)