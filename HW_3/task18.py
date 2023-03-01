# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

N = int(input("Введите количество элементов в массиве: "))

A = [random.randrange(10) for _ in range(N)]
print(f'{A = }')
x = int(input("введите число: "))

nearest_to_x = A[0]
dif_min = abs(x - A[0])

for i in range(1, len(A)):
    dif = abs(x - A[i])
    if dif < dif_min:
        dif_min = dif
        nearest_to_x = A[i]
    
print(f'ближайшее к {x} число {nearest_to_x}')