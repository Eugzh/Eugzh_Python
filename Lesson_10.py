# def func(a, b=0):
#     return a+b
#
#
# print(func(2, 5))
# print(func(5, 2))
# print(func(2))

# lst = [1, 2, 3]
# lst2=[1, 2, 3]
# print(lst, id(lst))
# print(lst2, id(lst2))
# print(lst == lst2)
# print(lst is lst2)
#
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])

# a = tuple("Hello")

# a = (1, 2, 3, 4, 5, 6)
# print(a[2])
# print(a[1:3])

# print([i for i in range(10)])

# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
#
# print(t3.count("l"))
#
# def slicer (tpl, elem):
#     if elem in tpl:
#        if tpl.count(elem) == 1:
#            return tpl[tpl.index(elem):]
#
#        else:
#            first= tpl.index(elem)
#            second=tpl.index(elem, first + 1)
#            return tpl[first:second + 1]
#
#     else:
#         return ()
#
#
#
# print(slicer(tpl=(1,2,3), elem=8))
# print(slicer(tpl=(1,2,3,4,8,8,9,2), elem=8))
# print(slicer(tpl=(1,2,8,5,1,2,9), elem=8))
#
# t = (True, 11, "Python", [4, 5, 6], ["Hello", "World"])
# print(t, id(t))
# t[4][0] = "New"
# print(t, id(t))
# t[4].append("Hi")
# print(t, id(t))
#
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)
#
# def get_user():
#     name = "Tom"
#     age = 22
#     married = False
#     return name, age, married
#
# # user = get_user()
# # print(user)
#
# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)
#
# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Норвегия", 5.900, (("Осло", 709.037), ("Тронхейм", 212.660)))
# )
#
# # print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print(country_name, country_population, cities)
#     for city in cities:
#         city_name, city_population = city
#         print(city_name, city_population)
#
# tpl = tuple(input("Введите строку"))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#       lst.append(tpl[i])
# print(lst)
# for i in range(len(lst)):
#     print("Кол-во", lst[i], tpl.count(lst[i]))

