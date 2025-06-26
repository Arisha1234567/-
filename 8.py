def equation_of_line(values):
                                #Находит уравнение прямой, проходящей через заданные точки
    k = values[1] - values[0] # Вычисляем угловой коэффициент k

    # Проверяем, является ли последовательность арифметической прогрессией
    if any(values[i] - values[i - 1] != k for i in range(1, len(values))):
        return None # Не является прямой

    b = values[0] # Вычисляем свободный член b
    result = "y = "

    if k == 0: # Обрабатываем случай горизонтальной прямой
        return "y = 0" if b == 0 else f"y = {b}" if b > 0 else f"y = -{abs(b)}"

    if k == 1:
        result += "x"
    elif k == -1:
        result += "-x"
    else:
        result += f"{k}x"

    if b > 0:
        result += f" + {b}"
    elif b < 0:
        result += f" - {abs(b)}"

    return result



print(equation_of_line([0, 1, 2, 3, 4]))
print(equation_of_line([0, -1, -2, -3, -4]))
print(equation_of_line([0, -2, -4, -6, -8]))
print(equation_of_line([1, 3, 5, 7, 9]))
print(equation_of_line([6, 6, 6, 6, 6]))
print(equation_of_line([1, 1, 2, 2, 2]))






