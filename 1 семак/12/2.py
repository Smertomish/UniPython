zero_element = float(input("Нулевой элемент: "))
difference = float(input("Знаменатель: "))
n = int(input("Количество членов: "))


def sum_geom_progr(q, n, zero):
    if n == 0:
        return 0
    return zero + sum_geom_progr(q, n-1, zero*q )


print(sum_geom_progr(difference, n, zero_element))