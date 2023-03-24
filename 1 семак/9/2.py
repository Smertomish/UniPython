import re

sentences = open("sentences.txt", encoding="UTF-8").readline()

sentences1 = sentences.replace("!", "^!^").replace("?", "^?^").replace(".", "^.^")
sentences1 = re.split(" |\^", sentences1)
sentences2 = [value for value in sentences1 if value]

new_txt = ''
k = 0
current_sentence = ''
num = int(input("Ваше минимальное количество слов: "))
for word in sentences2:
    if word in ".!?":
        if k > num:
            new_txt += current_sentence + word
        k = 0
        current_sentence = ''
    else:
        k += 1
        current_sentence += " " + str(word)

print(new_txt)
res = open("res.txt", "w+", encoding="UTF-8")
res = open("res.txt", "a+", encoding="UTF-8")
res.write(new_txt)