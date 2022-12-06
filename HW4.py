# 1.	Вычислить число c заданной точностью d
#Пример:при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
# d = int(input('введите количество знаков после запятой '))
# n = float(input('введите число '))
# # print(round((n), d))
# print('{0:.3f}'.format(n))
import math

pi = math.pi
print('Pi = ', pi)
d= float(input("Введите точность в формате 0.001 "))
# d = 0.001
print(f'Accuracy = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print(round(pi, count))

# 2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('введите число  '))
# count = 2
# for i in range(n):
#     if n % count == 0:
#         print(count, end='')
#         n = n/count
#
#     else:
#         #n % count != 0
#         count += 1
#
# 3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

# list = [1, 2, 2, 3, 4]
# lib = {}
# for el in list:
#      lib[el] = lib.get(el,0)+1
# print(lib)
# for key, value in lib.items():
#     if value <2:
#          print(key, end='')

# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# n = int(input('введите коэффициент '))
# list_konst = []
# for i in range(n+1):
#     k = random.randint(0, 101)
#     list_konst.append(k)
# print(list_konst)
# str = ''
# for i in range(n):
#
#     str += f'{list_konst[i]}x^{n}+'
#
#     n-=1
# str += f'{list_konst[i]}=0'
# print(str)
# with open('file.txt','w') as mnogochlen:
#     mnogochlen.write(str)


# 5.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

# print('задача 5')
#
# file = open('file.txt')
# line1 = file.readline()
# mnogochlen2 = open('mnogochlen2.txt')
# line2 = mnogochlen2.readline()
# line1 = line1.split('+')
# line2 = line2.split('+')
# print(line1)
# print(line2)
#
# koeff1=[]
# for i in range(len(line1)-1):
#     koeff_line1=int(line1[i][:-3])
#     koeff1.append(koeff_line1)
# koeff1.append(int(line1[-1][:-2]))
# print('коэффициенты первого уравнения')
# print(koeff1)
#
# koeff2=[]
# for i in range(len(line2)-1):
#     koeff_line2=int(line2[i][:-3])
#     koeff2.append(koeff_line2)
# koeff2.append(int(line2[-1][:-2]))
# print('коэффициенты второго уравнения')
# print(koeff2)
#
# result_koeff = []
# for i in range(len(line2)):
#     res_koeff = koeff1[i]+koeff2[i]
#     result_koeff.append(res_koeff)
# print('коэффициенты сложения')
# print(result_koeff)
#
# result_line = ''
# for i in range(len(result_koeff)-1):
#     result_line += f'{result_koeff[i]}x^{4-i}+'
#
#     n -= 1
# result_line += f'{result_koeff[-1]}=0'
# print(result_line)
# with open('result_mnogochlen.txt','w') as mnogochlen:
#     mnogochlen.write(result_line)
#
# file.close()
# mnogochlen2.close()
