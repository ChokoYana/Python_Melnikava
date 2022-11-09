# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# s_list = input().split(' ')
# print(s_list)
# d_list = []
# for i in s_list:
#     if 'abc' not in i:
#         d_list.append(i)
# print(d_list)

# ----------------------------------------------------------------------------



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('text.txt', 'r', encoding= 'UTF-8') as a:
#     s = a.readline()
#     print(s)
# encod = ""
# i = 0
# while i < len(s):
#     count = 1
#     while i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#         i += 1
#     encod += str(count) + s[i]
#     i+=1
# print(encod)
# with open('tex.txt', 'w') as b:
#     b.write(encod)


# ------------------------------------------------------------------

# with open('tex.txt', 'r', encoding= 'UTF-8') as a:
#     s = a.readline()
#     print(s)
# encod = ""
# i = 0
# while i < len(s):
#     count = 1
#     while i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#         i += 1
#     encod += str(count) + s[i]
#     i+=1
# print(encod)
# with open('text.txt', 'w') as b:
#     b.write(encod)


# with open('text11.txt', 'r', encoding= 'UTF-8') as a:
#     s = a.readline()
#     print(s)
# encod = ""
# i = 0
# count = 0
# while i < len(s):
#     if str(s[i]).isdigit():
#         count = int(s[i])
#         encod += s[i + 1] * count
#         i +=1
#     else:
#         i +=1
# print(encod)
# with open('text12.txt', 'w') as b:
#     b.write(encod)


# ________________________________________________________________________
# ________________________________________________________________________

# Задача с конфетами: 
# сделала сколько смогла и поняла.

# sugar = 200
# while sugar > 0:
#     player1= int(input('Игорок 1: Введите колличество конфет: '))
#     if player1 > 0 and player1 < 29:
#         if sugar < 28:
#             print('Первый игрок выиграл')
#             break
#         else:
#             sugar -= player1
#             print(sugar)
        
#     else:
#         print("не правильный ввод попробуйте снова")
#         continue
#     player2 = int(input('Игорок 2: Введите колличество конфет: '))
#     if player2 > 0 and player2 < 29:
#         if sugar < 28:
#             print('Второй игрок выиграл')
#             break
#         else:
#             sugar -= player2
#             print(sugar)
        
#     else:
#         print("не правильный ввод попробуйте снова")
#         continue


# ---------------------------------------------------------------

# sugar = 200
# while sugar > 0:
#     player1= int(input('Игорок 1: Введите колличество конфет: '))
#     if player1 > 0 and player1 < 29:
#         if sugar < 28:
#             print('Первый игрок выиграл')
            
#         else:
#             sugar -= player1
#             print(f"Остаток конфет: {sugar}")
#     else:
#         print("не правильный ввод попробуйте снова")
#         continue
#     player2 = 28
#     print(f'Компьютер взял {player2}')
#     if sugar > 57:
#         sugar -= player2
#         print(f"Остаток конфет: {sugar}")
            
            
#     elif sugar < 58 and sugar > 30:
#         player2 = sugar - 29
#         print(f'Компьютер взял {player2}')
#         print(f"Остаток конфет: {sugar}")
#     else:
#         player2 = sugar
#         print(f'Компьютер взял {player2}')
#         print('Компьютер выиграл')
#         break
    


