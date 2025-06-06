# d = {i: i ** 2 for i in range(1, 8)}
# print(d)
#
# print(25 in d)
# print(3 in d)
#
# del d[3]
# print(d)
#
# key = 8
# if key in d:
#     del key
# print(d)
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# for key in d:
#     print(key, ":", d[key])
#
# res = 1
#
# for key in d:
#     res *= d[key]
# print(res)

# d = {}
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}
# print(d)
#
# dislike = int(input("Какой элемент удалить?"))
# del d[dislike]
# print(d)
#
# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400]
#
#
# }
#
# for i in goods:
#     print(i, ")",goods[i][0],"-", goods[i][1], " Шт. по ", goods[i][2], "руб",  sep="")
#
# while True:
#     n = input("N ")
#     if n == "0":
#         break
#     else:
#         if i in goods:
#             while True:
#                 try:
#                  count = int(input("Кол-во: "))
#                  goods[n][1] += count
#             except ValueError:
#                 print("Значение некорректное")
#         else:
#             print("Такого ключа не существует")
#
#
#         print(i, ")", goods[i][0], "-", goods[i][1], " Шт. по ", goods[i][2], "руб", sep="")
#

# d = {"A": 1, "B": 2, "C": 3}
#
# print(dir(dict))
# print(d)
#
# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i, j in d.items():
#     print(i, ":", j)
#
# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 = ", d2)
# d2["B"] = 5
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # d.clear()
# # item = d.pop("B")
# item = d.popitem()
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # # print(d["W"])
# # value = d.get("W")
# # print(value)
# item = d.setdefault("W", 5)
# print(d)
# print(item)
#
# d = {"A": 1, "B": 2, "C": 3}
# d2 = {"R": 7, "Q": 9}
# print(d)
# print(d2)
# d3 = d | d2
# d.update(d2)
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
#
# print(d)
# print(new_d)
#
# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
# d["location"] = d.pop("city")
# print(d)
#
# d = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#
#     },
#     "second": {
#         4: "four",
#         5: "five"
#
#     }
# }
#
# print(d)
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ": ", d[x][y], sep="" )