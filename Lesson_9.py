# def hello(name, age):
#     print("Меня зовут " + name + ". Мне " + str(age) + " лет ")
#
#
# hello("Irina,", 28)
# hello("Ivan,", 15 )

# def get_sum(a, b):
#     print(a + b)
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum(a="abc", b="def")

#
# def print_line(count, a, b):
#    for i in range(count):
#        if i % 2 == 0:
#         print(a, end="")
#        else:
#            print(b, end="")
# print()
#
#
# print_line(count=9, a="+", b="-")
# print_line(count=7, a="X", b="0")

# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
#
# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(one=9, two=6))

# def calc(a, b):
#     if a > b:
#         return a + b
#     else:
#         return a - b
#
#
# a = int(input("Введите a"))
# b = int(input("Введите b"))
# print(calc(a, b))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print([9, 13, 33, 54, 105])
# print(["С", "л", "о", "н"])

# def get_sum(a, b, c=10, d=0):
#     return a + b + c + d
#
# print(get_sum(a=1, b=5))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info(name="igor", age=23, name= "Ira")