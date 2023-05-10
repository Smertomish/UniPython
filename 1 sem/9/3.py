file_in = '3.txt'
file_out = '3_3.txt'


def transposeMatrix(matrix):
    transpMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpMatrix[j][i] = matrix[i][j]
    return transpMatrix


with open(file_in, encoding='utf-8') as file:
    fileInfo = file.read()

matrix = []

for i in fileInfo.split('\n'):
    if len(i) > 0:
        try:
            row = list(map(int, i.split(' ')))
        except:
            print("Недопустимые данные в файле")
            exit()
        matrix.append(row)
    else:
        print("Некорректные данные")
        exit()

newMatrix = transposeMatrix(matrix)

file = open(file_out, encoding='utf-8', mode='w')

for row in newMatrix:
    for element in row:
        file.write(f'{str(element)} ')
    file.write('\n')
