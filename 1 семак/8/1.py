from statistics import mean

players = {'Иванов': 20, 'Сидоров': 68, 'Петров': 26, 'Смирнов': 68}
new_players = ''

print('Введите новых участников через enter')
print('Чтобы завершить ввод введите: завершить')
print('введите участника и его балл: ')

while new_players != 'завершить':
    new_players = input()
    if new_players != 'завершить':
        try:
            new_players = new_players.split()
            players.update({str(new_players[0]): int(new_players[1])})
        except:
            print('Предыдущий ввод не внесён в словарь из-за ошибки')
    else:
        break

min_value = min(players.values())
max_value = max(players.values())
mean_value = mean(players.values())

print('Минимальное значение получили')
for key, value in players.items():
    if value == min_value:
        print(key, value)

print('Максимальное значение получили')
for key, value in players.items():
    if value == max_value:
        print(key, value)

print('Среднее значение = ', mean_value)

print('Имена отличившихся:')
for key, value in players.items():
    if value > mean_value:
        print(key)
