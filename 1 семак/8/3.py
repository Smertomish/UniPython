dictionary = {'привет': 'hello', 'как': 'how', 'твоя': 'your', 'собака': 'dog'}

#new_dictionary = {}
#def invert():
#   for rus, eng in dictionary.items():


new_translate = '2'
happened = 0
print('\nВведите пустую строку, если не хотите обновлять словарь')
while new_translate:

    new_translate = input('Введите новый перевод (rus eng)\n')
    try:
        new_translate = new_translate.split()
        dictionary.update({str(new_translate[0]): str(new_translate[1])})
    except:
        if new_translate:
            print('Предыдущий ввод не внесён в словарь из-за ошибки')


str = input('Введите ваше предложение:\n').lower().split()
translated_str = ''

for word in str:
    if word in dictionary.keys():
        translated_str += dictionary[word] + ' '
    else:
        translated_str += word + ' '

if translated_str:
    print(translated_str)
else:
    print('Строка не изменилась')