# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# s_list = input().split(' ')
# print(s_list)
# d_list = []
# for i in s_list:
#     if 'abc' not in i:
#         d_list.append(i)
# print(d_list)







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

