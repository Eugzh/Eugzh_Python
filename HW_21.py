f = open("test.txt")
print(*f)
print(f)
print(f.mode)
print(f.name)
print(f.encoding)

f.close()
print(f.closed)

f = open("text.txt", "r")
print(f.read(3))
f.close()
