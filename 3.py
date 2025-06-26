def get_quadrant(p):
    x, y = p # Распаковка кортежа p в переменные x и y
    if x > 0 and y > 0:
        return 1 # Первая четверть
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return None  # Точка лежит на оси координат
print(get_quadrant((3, 4)))
print(get_quadrant((-1, 2)))
print(get_quadrant((-3, -5)))
print(get_quadrant((1, -1)))