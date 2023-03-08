# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def summ (a, b):
    if a == 0:
        return b
    return summ(a - 1, b) + 1

print(summ(6, 10))
