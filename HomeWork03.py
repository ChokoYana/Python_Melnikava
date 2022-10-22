# Задайте список из нескольких чисел.  Напишите программу, 
# которая найдёт сумму  элементов списка, стоящих на нечётной позиции.


# a = []
# a = [int(i) for i in input('Введите массив через пробел: ').split()]
# print(a)
# i = 1
# sum = 0
# while i < len(a):
#     sum += a[i]
#     i +=2
# print(sum)


# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# n = int(input('Введите размер массива: '))
# a = []
# a = [int(input("Введите эллемент массива и нажмите 'enter' : ")) for _ in range(n)]
# print(a)
# list = []
# for idx in range((n - 1) // 2 + 1):
#     list.append((a[idx]) * (a[n - idx - 1]))
# print(list)




# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.



# n = int(input('Введите размер массива: '))
# a = []
# a = [float(input("Введите эллемент массива и нажмите 'enter' : ")) for _ in range(n)]
# print(a)
# for idx in range(n):
#     a[idx] = round(a[idx] - int(a[idx]), 2)
# print(a)
# for idx in range(n - 1):
#     if a[idx] == 0:
#         a.pop(idx)
# print(a)
# max_num = max(a)
# min_num = min(a)
# print(max_num - min_num)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# a = int(input('Введите число: '))
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)



# a = int(input())
# a = format(a, 'b')
# print(a)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# k = int(input('Введите число: '))
# a_list = [0] * (k * 2 + 1)
# a_list[k + 1] = 1
# for idx in range(k + 2, k * 2 + 1):
#     a_list[idx] = a_list[idx - 1] + a_list[idx - 2]
# print(a_list)
# for idx in range(k, -1, -1):
#     a_list[idx] = a_list[idx  + 2] - a_list[idx +1]
# print(a_list)