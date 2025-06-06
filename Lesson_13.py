# d = {"Один": 1, "Два": 2, "Три": 3, "Четыре": 4}
# print({k: v for k, v in d.items() if v <= 2})

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i* 3 for i in s}
# print(d1)
#
# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d ={}
# s = None
#
# for i in lst:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)
#
# d = dict(zip([1, 2, 3], ["one", "two", "three"]))
# print(d)
#
# d1 = list (zip ([1, 2, 3], ["one", "two", "three"]))
# print(d1)
#
# a = [1, 2, 3]
# b = ["one", "two", "three"]
# d = {k: v for k, v in zip(a, b)}
# print(d)

# a = [1, 2, 3]
# c = list(zip(a))
# print(c)
#
# one = {"name": "Igor", "surname": "Pavlov", "job": "consultant"}
# two = {"name": "Irina", "surname": "Petrova", "job": "manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#
# lst = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
# a, b = zip(*lst)
# print(a)
# print(b)
#
# letter = ["a", "b", "d", "c"]
# number = [3, 4, 2, 1]
# d = dict(zip(letter, number))
# print(d)
#
# data2 = list(zip(letter, number))
# print(data2)
# data2.sort()
# print(data2)
#
# d2 = dict(data2)
# print(d2)
#
# d3 = {v: k for k, v in data2}
# print(d3)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
#
# one = {"Один": 1, "Два": 2}
# two = {"Три": 3, "Четыре": 4}
# print({**one, **two})
#
# colors = ["red", "yellow", "green"]
# i = 1
#
# for color in colors:
#     print(i, ") ", color, sep= "")
#     i += 1
# print()
# for j, color in enumerate(colors, 1):
#     print(j, ") ", color, sep="")
#
# d = {"Один": 1, "Два": 2, "Три": 3, "Четыре": 4}
#
# for i, (k, v) in enumerate(d.items()):
#     print(i, ") ", k, ": ", v,  sep="")
#
# def func(args):
#     return args
# print(func(5))
#
# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa( 7, 8, 9))

def average(*args):
    sr = sum(args) / len(args)
    print(sr)

    res = []
    for num in args:
        if num < sr:
            res.append(num)

    return res
print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(average(3, 6, 1, 9, 5))