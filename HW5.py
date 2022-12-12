# 1.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

# sp = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']
# res = list(filter(lambda x:'АБВ' not in x,sp))
# print(res)

# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# n = 100
#
# while n > 28:
#     a = int(input('сколько берете конфет '))
#     if a > 28:
#         print('вы взяли слишком много')
#     else:
#         n -= a
# if n < 28:
#     print('выиграл следующий игрок')

# a) Добавьте игру против бота

#здесь первым ходит игрок
#
# import random
# n = 100
# a = int(input('сколько берете конфет '))
# if a > 28:
#     print('вы взяли слишком много')
#
# else:
#     n -= a
#     bot = n % 29
#     if bot == 0:
#         bot = random.randint(1,28)
#     n-=bot
#     print(f'компьютер взял {bot}')
# while n != 0:
#     a = int(input('сколько берете конфет '))
#     if a > 28:
#         print('вы взяли слишком много')
#     else:
#         n -= a
#         bot = n % 29
#         print(f'компьютер взял {bot}')
#         n -= bot
#     if 0 < n <= 28:
#         bot = n
#         # n -= bot
# print('и выиграл')

#3.	Создайте программу для игры в "Крестики-нолики".

# map=[1,2,3,
#      4,5,6,
#      7,8,9]
# def print_map():
#      print(map[0], end=" ")
#      print(map[1], end=" ")
#      print(map[2])
#
#      print(map[3], end=" ")
#      print(map[4], end=" ")
#      print(map[5])
#
#      print(map[6], end=" ")
#      print(map[7], end=" ")
#      print(map[8])
# print_map()
# count = 0
# game_over = False
# while game_over == False and count < 8:
#       step1 = False
#       step2 = False
#       while step1==False:
#           i = int(input('куда ставим X '))
#           if map[i-1] =='X' or map[i-1] =='O':
#                print('место уже занято')
#                step1 = False
#           else:
#                map[i - 1] = 'X'
#                print_map()
#                step1 = True
#       if map[0] == map[1] == map[2] or map[3] == map[4] == map[5] or \
#           map[6] == map[7] == map[8] or map[0] == map[4] == map[8] or \
#           map[2] == map[4] == map[6]:
#           print('WIN!')
#           game_over = True
#       count +=1
#       while step2 == False:
#           # while step2 == False:
#           i = int(input('куда ставим O '))
#           if map[i-1] =='X' or map[i-1] =='O':
#                print('место уже занято')
#                step2 = False
#           else:
#                map[i - 1] = 'O'
#                print_map()
#                step2 = True
#       if map[0] == map[1] == map[2] or map[3] == map[4] == map[5] or \
#           map[6] == map[7] == map[8] or map[0] == map[4] == map[8] or \
#           map[2] == map[4] == map[6]:
#           print('WIN!')
#           game_over = True
#       count += 1
# print('NO WIN')

#4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Пример:
#Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#Текст после кодировки: 12W1B12W3B24W1B14W
#Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#Входные и выходные данные хранятся в отдельных текстовых файлах.

# cod = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# res_str = ''
# for i in range(len(cod)-1):
#     count = 1
#     char = cod[0]
#     if char == cod[i]:
#         count += 1
#     else:
#         res_str += str(count)+char
#
#         char = cod[i]
#         count = 1
#
#     res_str += str(count)+char
# print(res_str)

#
# for i in range(2, len(cod)):
#     count = 1
#     while cod[i] == cod[i-1]:
#         count += 1
#     res_str += str(count)+cod[i]
# print(res_str)