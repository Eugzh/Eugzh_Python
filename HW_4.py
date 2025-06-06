num = int(input("Введите количество символов"))
symbol = input("Введите тип символа")
line = int(input("Выберите тип ориентации"))
i = 0
while i < num:
    if line == 0:
        print(symbol)
    else:
        print(symbol, end=" ")
        i += 1





