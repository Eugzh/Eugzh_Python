start = [1, 3, 7, 8, 7, 5, 5, 4]
end = []

for i in range(len(start)):
    if start.count(start[i]) == 1:
        end.append(start[i])
print(end)