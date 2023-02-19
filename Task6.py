# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

num = int(input('введите номер билета: '))

a = int(num / 1000)
b = num % 1000
sum_a = int(a / 100) + a % 10 + a % 100 / 10
sum_b = int(b / 100) + b % 10 + b % 100 / 10

print(int(sum_a) == int(sum_b))