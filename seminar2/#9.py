#4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N=int(input('введите N= '))
list=[]
for i in range(-N,N+1):
    list.append(i)
print(list)

file=open("file.txt")

i=0
multipl=1
for i in open("file.txt"):
    x=int(file.readline())
    multipl*=list[x]
print(multipl)