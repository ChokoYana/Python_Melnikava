#Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.

# a = int(input("Введите число обозначающее день недели: "))
# if a < 6:
#     print("Это рабочий день!")
# elif a > 7:
#     print("Введеное число не соответсвует дню недели")
# else:
#     print("Это выходной!")



# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             print(x, y, z, end= ' : ')
#             print(not(x or y or z) == ((not x) and (not y) and (not z)))            

# Напишите программу, которая принимает на вход координаты
#  точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# x = int(input('Введите координату X: '))
# y = int(input('Введите координату Y: '))

# if x > 0 and y > 0:
#     print('Ваша координата находится в плоскости 1')
# elif x > 0 and y < 0:
#     print('Ваша координата находится в плоскости 4')
# elif x < 0 and y < 0:
#     print('Ваша координата находится в плоскости 3')
# else:
#     print('Ваша координата находится в плоскости 2')


# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

# a = int(input('Введите номер четверти: '))
# if a < 2:
#     print('Диапазон координат: x > 0  и y > 0')
# elif 1 < a < 3:
#     print('Диапазон координат: x < 0  и y > 0')
# elif 2 < a < 4:
#     print('Диапазон координат: x < 0  и y < 0')
# elif 3 < a < 5:
#     print('Диапазон координат: x > 0  и y < 0')
# else:
#     print('Вы вышли за значение номера четверти')



# Напишите программу, которая принимает на 
# вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# x1 = int(input('Введите координуту х первой точки: '))
# y1 = int(input('Введите координуту y первой точки: '))
# x2 = int(input('Введите координуту х второй точки: '))
# y2 = int(input('Введите координуту y второй точки: '))

# len = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)
# print(f'Длинна отрезка ваших координат {len}')
