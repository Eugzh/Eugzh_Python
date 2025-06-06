# lst = [11, 1, 22, 2, 33, 3, 55, 66]
# lst [5:] = []
# print(lst)

# lst.remove(22)
# print(lst)
#
# last = lst.pop()
# print(last)
# print(lst)

# lst.clear()
# print(lst)

# a = [int(input("->")) for i in range(int(input("n =")))]
# k = int(input("k ="))
# a.pop(k)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 55, 66]
# value = 100
# if value in lst:
#     ind = lst.index(33)
#     print(lst)
# print(ind)

# lst = [11, 1, 22, 2, 33, 3, 55, 66]
# a = lst.copy()
# print(a)
# print(lst)
#
# a.append(100)
# print(lst)
# print(a)
# lst[0] = 256

# lst = [11, 1, 22, 2, 33, 3, 55, 66]
# lst.reverse()
# print(lst)
#
# lst = [11, 1, 22, 2, 33, 3, 55, 66]
# lst.sort(reverse=True)
# print(lst)
#
# st = "Hello"
# new_lst = sorted(lst, reverse=True)
# print(new_lst)

import random
#
# print(random.random())
# print((random.randint(a=5, b=10)))
# print(random.randrange(start=5, stop=10))
# print(random.uniform(a=10.5, b=25.5))
#
# city_list = ['Moscow', 'Novosibirsk', 'Voronezh', 'Sochi',]
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
#
# # print(random.choice(city_list))
# # print(random.choice(s))
# # print(random.choices(city_list, k=3))
# # print(random.choices(s, k=3))
# random.shuffle(city_list)
# random.shuffle(s)
# print(city_list)
# print(s)

mas = [random.randint(a=0, b=100) for i in  range(10)]
print(mas)