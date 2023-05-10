from random import randint


y = int(input("Введите кол-во строк матрицы А: "))
x = int(input("Введите кол-во столбцов матрицы А: "))

xB = int(input("Введите кол-во столбцов матрицы B: "))

matrixA = [[0 for j in range(x)] for i in range(y)]
for i in range(y):
    for j in range(x):
        matrixA[i][j] = randint(-9, 9)

matrixB = [[0 for j in range(xB)] for i in range(x)]
for i in range(x):
    for j in range(xB):
        matrixB[i][j] = randint(-9, 9)


matrixC = [[0 for j in range(xB)] for i in range(y)]
for i in range(y):
    for j in range(xB):
        for k in range(x):
            matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

print("Матрица A")
for i in range(y):
    for j in range(x):
        print(matrixA[i][j], end=' ')
    print()

print("Матрица В")
for i in range(x):
    for j in range(xB):
        print(matrixB[i][j], end=' ')
    print()

print("Матрица C")
for i in range(y):
    for j in range(xB):
        print(matrixC[i][j], end=' ')
    print()
