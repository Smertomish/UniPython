line = input("Введите массив: ").split()
count = [0] * 10
break_ = True
for i in range(len(line)):
    try:
        digit = int(line[i])
    except:
        break_ = False
        print("В вашем массиве есть не только числа")
        break
    count[digit] += 1

if break_:
    c1 = 0
    max_count = max(count)
    for i in count:
        if i == max_count:
            c1 += 1
    if c1 == 1:
        print("Мода = ", count.index(max_count))
    else:
        print("Моды нет")
