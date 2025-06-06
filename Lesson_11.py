# s = {"red", "yellow", "green"}
# print(s)
# print(type(s))

# a = set()
# print(a, type(a))

# s = {i * i for i in range(10)}
# print(s)
#
# lst = [8, 8, 0, 3, 3, 3, 2, 6, 0, 5]
# print({i for i in lst if i % 2 == 0})

# t ={"red", "green", "Yellow"}
# print("green" in t)
# print("blue" in t)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if "a" in i])
# print(tuple("A" if i[0] == "a" else "B" for i in lst))
# print(["A" + i [1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
#
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
#
# print(lst2)

# a = {"red", "yellow", "green"}
#
# a.add("Black")
# print(a)
#
# a.remove("yellow")
# print(a)
#
# el = "green"
# if el in a:
#     a.remove(el)
#     print(a)
#
# a.discard("yellow")
# print(a)
#
# a.pop()
# print(a)
#
# a.clear()
# print(a)
#
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# c = a & b
# print(c)
# c = a - b
# print(c)
# c = a ^ b
# print(c)

# s1 = {1,2}
# s2 = {3}
# s3 = {4,5}
# s4 = {3,2,6}
# s5 = {6}
# s6 = {7,8}
# s7 = {9,8}
#
# unit = s1 |s2 | s3 | s4 | s5 | s6 | s7
# unit2 = s1.union(s2, s3, s4, s5, s6, s7)
# print(unit2)
# print(unit)
# print("Уникальные элементы:", len(unit))
# print("Максимальное число:", max(unit))
# print("Минимальное число:", min(unit))
#
# s1 = "Hello"
# s2 = "How are you"
#
# a = set(s1) & set(s2)
# print(a)
#
# for i in a:
#     print(i, end=" ")
#
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# print(c)
# c2 = a <= b
# print(c2)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
#
# print(lst)
# print(d)
#
# print(lst[1])
# lst[1] = "ten"
# print(lst)
#
# d["second"] = "ten"
# print(d)
#
# d = dict(a = "Hello", b = "World")
# print(d)
# print(type(d))
#
# d1 = {"a": "Hello", "b": "World"}
# print(d1)

d = {0: "text"}
print(d)

d2 = {"One": 45}
print(d2)