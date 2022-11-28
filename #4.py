# 4.	Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)
import sys
Quarter = int(input('введите четверть = '))
if Quarter > 4 or Quarter < 1:
    print('введите другое число')
    sys.exit()
if Quarter == 1:
    print('x>0, y>0')
elif Quarter == 2:
    print('x<0, y>0')
elif Quarter == 3:
    print('x<0, y<0')
else:
    print('x>0, y<0')
