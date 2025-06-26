def linear_coefficients(p1, p2): # функция для вычисления коэффициентов линейного уравнения
    x1, y1 = p1 # распаковка координат первой точки
    x2, y2 = p2 # распаковка координат второй точки
    if x1 == x2: # проверка на вертикальную линию
        return None, x1 # возвращает None, x для вертикальной линии
    else:
        k = (y2 - y1)/(x2 - x1) # вычисление k
        b = y1 - k * x1 # вычисление b
        return k, b # возвращает k, b
print(linear_coefficients((1, 2), (2, 3)))
print(linear_coefficients((0, 0), (1, 5)))
print(linear_coefficients((0, 2), (2, 2)))
print(linear_coefficients((-2, -2), (-1, -2)))
print(linear_coefficients((1, -1), (-1, 1)))
print(linear_coefficients((2, 2), (3, 3)))