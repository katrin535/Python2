'''Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 '''

a = int(input('Введите число А, которое нужно возвести в степень: '))
b = int(input('Введите степень В: '))

def recAB(a, b):
    if b == 0:
        return 1
    return a * recAB(a, b - 1)

print('Число A в степени B: ', recAB(a, b))