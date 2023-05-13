'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 '''

a = int(input('Введите число А >= 0: '))
b = int(input('Введите число В >= 0: '))

def recSum(a, b):
    if a == 0:
        return b
    return recSum(a - 1, b + 1)

print('Сумма неотрицательных чисел: ', recSum(a, b))