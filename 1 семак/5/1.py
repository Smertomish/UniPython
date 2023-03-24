file_extension_3 = ['txt', 'doc', 'odt', 'rtf']
symbols = ['<', '>', '\\', '|', '/', '?']


# Проверка расширения файла
def check_extension(line_):
    if line_[-4] == '.' and (line_[-3:-1] + line_[-1]) in file_extension_3:
        return True
    if line_[-5] == '.' and (line_[-4:-1] + line_[-1]) == 'docx':
        return True
    else:
        return False


# проверка содержания ошибочных символов в названии
def check_symbols_errors(line_):
    for i in line_:
        if i in symbols:
            return False
    return True


line = '1'
while len(line) > 0:
    print("Введите строку")
    line = input()
    if line:
        if check_extension(line) and check_symbols_errors(line) and len(line) > 4:
            print("Хорошее название для файла")
        else:
            print("Такое название не подходит")

if not line:
    print("Строка должна содержать символы")
    print("Программа завершила свою работу.")
    exit()
