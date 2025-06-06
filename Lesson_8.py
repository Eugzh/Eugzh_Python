import random

# mas = [random.randint(a=0, b=100) for i in range(10)]
# print(mas)

# print(len(mas)) #Длина списка
# print(min(mas)) #Минимальный элемент списка
# print(max(mas)) #Максимальный элемент списка
# print(sum(mas)) #Сумма элементов списка

# mas = [random.randint(a=0, b=100) for i in range(10)]
# print(mas)
# maximum = max(mas)
# print("Max =" , maximum)
# mas.remove(maximum)
# mas.insert(0, maximum)
# print(mas)

# mas = [random.randint(a=0, b=10) for i in range(10)]
# print(mas)
# print(2 not in mas)

# lst = []
# if len(lst) == 0:
#     print("Список пуст")

# print(bool(lst))
#
# if not lst:
#     print("Список пуст")
# else:
#     print("В списке есть элементы")

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1] [2])

# print("Вариант 1")
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row] [col], end="\t")
#     print()

# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# Модули

# import math
#
# print(math.sqrt(4))  #Корень квадратный
# print(math.ceil(3.2)) #Округление вверх
# print(math.floor(3.8)) #Округление вниз

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

from math import pi
rad = int (input("Введите радиус окружности"))
D = 2 * pi * rad
print(D)