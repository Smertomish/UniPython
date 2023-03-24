line = input("Введите массив: ").split()
line1 = ''
count = 0
max_count = 0


for x in range(len(line)):
    i = line[x]
    i = float(i)

    if i == 0:
        count += 1
        if max_count < count:
            max_count = count
            id0 = x - count + 1
    else:
        count = 0


print("\nсамая длинная последовательность из нулей = ", max_count)
print("индекс = ", id0)