def draw_graph(f):
    size = 10 # Размер графика
    height = size + 1 # Высота графика с учетом осей
    width = size * 3 + 4 # Ширина графика с учетом осей и меток
    screen = [[' ' for _ in range(width)] for _ in range(height)] # Создание пустого экрана
    y_axis_col = 3 # Координата столбца оси Y

    for y in range(height): # Рисование вертикальной оси Y
        screen[y][y_axis_col] = '|'

    for x in range(y_axis_col, width): # Рисование горизонтальной оси X
        screen[height - 1][x] = '-'

    screen[height - 1][y_axis_col] = '+' # Рисование точки пересечения осей

    for y in range(size + 1): # Рисование меток на оси Y
        val = size - y
        if val % 3 == 0: # Метка каждые 3 единицы
            line_idx = y
            label = str(val)
            label_pos = y_axis_col - len(label) // 2 # Центрирование метки

            for i, ch in enumerate(label):
                screen[line_idx][label_pos + i] = ch

    for x in range(0, size + 1, 3): # Рисование меток на оси X
        col = y_axis_col + 1 + x * 3
        label = str(x)
        label_pos = col - len(label) // 2 # Центрирование метки

        for i, ch in enumerate(label):
            screen[height - 1][col + i] = ch

    for x in range(size + 1): # Рисование графика
        y_val = f(x)
        if 0 <= y_val <= size: # Проверка, чтобы точка оставалась на экране
            row = height - 2 - y_val
            col = y_axis_col + 1 + x * 3
            screen[row][col] = '*'

    for row in screen: # Вывод графика на экран
        print(''.join(row))


def f(x): # Определяем функцию
    if x <= 5:
        return x
    return x - 2 * (x % 5)

draw_graph(f)
