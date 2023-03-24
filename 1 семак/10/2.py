with open("task3.txt", encoding="UTF-8") as file:
    file = file.read().splitlines()
print("\n***Изначальный файл:")
for i in file:
    print(i)

dic = {}
for word in file:
    k = 0
    for letter in word:
        if letter == 'а':
            k += 1
    if k in dic.keys():
        dic[k].append(word)
    else:
        dic.update({k: [word]})

print("\n***Результат:")
sor = sorted(dic.keys())
for i in range(len(sor), 0, -1):
    r = dic[i]
    for u in r:
        print(u)
