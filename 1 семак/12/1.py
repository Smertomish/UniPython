zero_element = float(input("Нулевой элемент: "))
difference = float(input("Знаменатель: "))
n = int(input("Количество членов: "))


def rec(el, step, counter):
    counter -= 1
    if counter == 0:
        return el
    else:
        el *= step
        return rec(el, step, counter)


print(rec(zero_element, difference, n))
