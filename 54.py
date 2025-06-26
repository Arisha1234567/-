def is_value(values, target):
    # Проверяем, равен ли первый элемент целевому значению
    if values[0] == target:
        return True

    i = 1
    # Удвигаем индекс в два раза, пока не найдем элемент, меньше целевого
    while i < len(values) and values[i] > target:
        i *= 2

    # Устанавливаем границы для бинарного поиска
    left = i // 2
    right = min(i, len(values) - 1)

    # Бинарный поиск целевого значения
    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            return True
        elif values[mid] > target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Примеры значений
values1 = [4, -3, -10, -17, -24, -31, -38, -45]
values2 = [1, 0, -3, -8, -15, -24, -35, -48, -63, -80, -99, -120, -143, -168]

print(is_value(values1, -17))
print(is_value(values1, 100))
print(is_value(values1, 4))
print(is_value(values2, -15))
print(is_value(values2, -159999))
print(is_value(values2, -640000))