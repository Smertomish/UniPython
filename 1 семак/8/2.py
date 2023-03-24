library = {'Джон': ['Кто такой настоящий мужчина'], 'Рон': ['Моя большая знакомая'], 'Марина': ['Пять одноглазых ребят']}

_end_ = ''

print('\nЧтобы закончить работу, введите: завершить\n')

while _end_ != 'завершить':

    new_author = str(input('Введите автора: \n'))

    if new_author in library.keys():
        print('\nВ библиотеке уже есть книги от этого автора:')
    for author, book in library.items():
        if new_author == author:
            for one_book in library[author]:
                print('**' + one_book + '**')
    new_book = str(input('\nВведите название книги, которую хотите добавить:\n'))
    try:
        library[new_author].append(new_book)
    except:
        library.update({new_author: [new_book]})

    print('книга успешно добавлена!\n')
    print('Теперь библиотека выглядит так: \n')
    for author, book in library.items():
        print(author, book)