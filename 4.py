def is_point_in_rectangle(p, rect) :
    x, y = p
    (x1, y1), (x2, y2) = rect

    if x1 < x < x2 and y1 < y < y2 : #проверка
        return True #если точка внутри прям
    else :
        return False
print(is_point_in_rectangle((1, 0), [(1, 1), (3, 4)]))
print(is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]))
print(is_point_in_rectangle((2, 1), [(1, 1), (3, 4)]))
print(is_point_in_rectangle((0, 0), [(-1, -1), (3, 3)]))