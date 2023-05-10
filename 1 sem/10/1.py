import copy

list = '132371235849840'
numbers = [int(value) for value in list]
numbers1 = copy.copy(numbers)
print(numbers)

# метод пузырька
length = len(numbers)
for i in range(length):
    for j in range(1, length):
        if numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
print(numbers)
print(sorted(numbers1))