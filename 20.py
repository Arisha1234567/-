def hamming_distance(s1: str, s2: str) -> int:
    # Проверяем, имеют ли строки одинаковую длину
    if len(s1) != len(s2):
        return -1  # Если нет, возвращаем -1

    distance = 0  # Инициализируем расстояние
    # Итерируем по символам строк
    for i in range(len(s1)):
        if s1[i] != s2[i]:  # Если символы различаются
            distance += 1  # Увеличиваем расстояние
    return distance  # Возвращаем итоговое расстояние

print(hamming_distance('abbcace', 'abacacc'))
print(hamming_distance('beegeek', 'beegeek'))
print(hamming_distance('abcd', 'efgh'))

