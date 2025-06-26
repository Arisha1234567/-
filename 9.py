def mid_num(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]
#находим среднее число из трёх
print(mid_num(1, 2, 3))
print(mid_num(3, 1, 2))
print(mid_num(-2, -3, -1))
print(mid_num(7, 7, 7))
print(mid_num(0, 0, 0))
print(mid_num(0, 0, 1))



