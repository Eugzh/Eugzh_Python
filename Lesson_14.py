# def func1(*args):
#     print("args:", args)
#     print(args[0])
#
#
#
#
#
# def func2(**kwargs):
#     print("kwargs:", kwargs)
#     print(kwargs["one"])
#
#
#
# func1(1,2,3,4,5,6)
# func2(one = 123, two=456)
#
# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"
#     print("hello", name, surname)
#
# def bye():
#     print("Goodbye", name)
#
# print(name)
# hi()
# bye()
# print(name)

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)
#
# print = 5
#
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(lst))
#
# x = 4
#
#
# def func():
#     x = 2
#
#     def inner():
#         print("x =", x)
#         print(x + 3)
#
#     inner()
# func()
#
# def outer(who):
#     def inner():
#         print("Hello", who)
#     inner()
#
#
# outer("World")

#
# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма:", a + b)
#     print("a:", a )
#     fun2(3)
#
# fun1()

#
# x = 25
#
# def fn():
#     global t
#     a = 30
#     def inner():
#         nonlocal a
#         a = 35
#         print("a=", a)
#     inner()
#     t = a
# fn()
# c = x + t
# print(c)

# x = 5
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x=", x)
#     fn2()
#     print("fn1.x=", x)
# fn1()
# print(x)
