def drop_one_and_five(n):
    result = 0  # Инициализация результата
    multiplier = 1  # Инициализация множителя для позиции цифры
    while n > 0:  # Пока число больше 0
        digit = n % 10  # Получаем последнюю цифру числа
        n //= 10  # Убираем последнюю цифру из числа
        if digit != 1 and digit != 5:  # Если цифра не 1 и не 5
            result += digit * multiplier  # Добавляем цифру в результат с учетом множителя
            multiplier *= 10  # Увеличиваем множитель на порядок
    return result  # Возвращаем итоговый результат

print(drop_one_and_five(527012))
print(drop_one_and_five(2468))
print(drop_one_and_five(0))
print(drop_one_and_five(1155))
print(drop_one_and_five(10))
print(drop_one_and_five(105))
