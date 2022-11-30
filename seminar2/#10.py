# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя,
#  другие методы из библиотеки random - можно).#
# import random
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.sample(list1, 9))


import random
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_index = len(list1) - 1
while last_index > 0:
    rand_index = random.randint(0, last_index)
    list1[last_index], list1[rand_index] = list1[rand_index], list1[last_index]
    last_index -= 1
print(list1)
