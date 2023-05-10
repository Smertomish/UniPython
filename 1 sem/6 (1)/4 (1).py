line = input("Введите строку: ")
line = line.split(' ')
new_line = [value for value in line if value]
count_upper = 0
count_dot = 0
for value in new_line:
    str_1 = value[0]
    if str_1.isupper():
        count_upper += 1
    if value[-1] in '.,:;!?':
        count_dot += 1

print('с заглавной: ', count_upper)
print('со знаком: ', count_dot)
