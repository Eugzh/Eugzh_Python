# def func(x, y):
#     return x+ y
#
#
# print(func(1, 3))
#
# print((lambda x, y: x + y)(1, 3))
#
# func = lambda x, y: x + y
#
# print(func(1, 3))
#
# func = (lambda x, y: x + y)(1, 3)
# print(func)
#
# print((lambda a, b, c: a + b +c)(10, 20, 30))
#
# print((lambda *args: sum(args))( 1, 2, 3, 4))

# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for t in tpl:
#     print(t("abc___"))
#
# def outer(n):
#     def inner(x):
#         return n +x
#     return  inner
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return  lambda x: n +x
#
# f = outer(42)
# print(f(3))
#
# outer = lambda n: lambda x: n + x
# f = outer(42)
# print(f(3))
#
# print((lambda n: lambda x: n + x)(42)(3))

# print((lambda a: lambda b: lambda c: a+b+c )(2)(4)(6))
#
# def func(i):
#     return i[i]
#
# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
#
# players = [
#     {'name': 'Антон', 'Last name': 'Бирюков', 'rating': 9 },
#     {'name': 'Алексей', 'Last name': 'Бодня', 'rating': 10},
#     {'name': 'Фёдор', 'Last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'Last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)
#
# lst = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]
#
# print(lst[0](12, 6))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[2]()
#
# def mult(t):
#     return t * 2
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t + 2, lst)))

# t = (2.88, -1.75, 100.55)
# #
# # print(tuple(map(lambda x: int(x), t)))
# # print(tuple(map(int, t)))
# # print(tuple(map(round, t)))
#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(dict(map(lambda x, y: (x, y), st, num)))
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("->") for i in range(5)]
# print(lst)
# lst = list(map(int, lst))
# print(lst)

