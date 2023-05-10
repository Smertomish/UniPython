def delete(num, vec):
    length = len(vec)
    for i in range(length - 1, length - num - 1, -1):
        vec.pop(i)
    return vec


file = open("vector.txt")
try:
    vec = list(map(int, file.readlines()))
    k = 1
except:
    print("В изначальном файле есть не число")
    k = 0
file.close()

if k == 1:
    try:
        del_count = int(input('Сколько чисел удалить?\n'))
        new_vec = delete(del_count, vec)
        res = open("BabyFile.txt", "w+")
        for i in new_vec:
            res = open("BabyFile.txt", "a+")
            res.write(str(i) + "\n")
    except ValueError:
        print("Введено не число")
