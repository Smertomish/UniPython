a = input("Введите координаты вектора а: ").split()
b = input("Введите координаты вектора b: ").split()

ans = 0
for i in range(len(a)):

    a_1 = int(a[i])
    b_1 = int(b[i])

    ans += a_1 * b_1

print(ans)
