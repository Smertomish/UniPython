number = int(input("Введите десятичное число: "))


def convertToBin(number):
    if number == 0:
        return '0'
    else:
        return str(convertToBin(number // 2)) + str(number % 2)


convertedNum = str(convertToBin(number))
if convertedNum != 0:
    convertedNum = convertedNum[1:]

print(convertedNum)
