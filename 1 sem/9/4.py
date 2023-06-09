import re

file_in = '4.txt'
file_out = '4_4.txt'


with open(file_in, encoding='utf-8') as file:
    fileInfo = file.read()

try:
    chapters = [chapter.strip() for chapter in fileInfo.split('Chapter') if chapter]
except:
    print("Недопустимые данные в файле")
    exit()

file = open(file_out, encoding='utf-8', mode='w')
file.write('Оглавление:\n')

for i in chapters:
    words = [word for word in re.split(r'\n+', i)]

    number = words[0]
    name = words[1]

    file.write(f'Глава {number}. {name}\n')