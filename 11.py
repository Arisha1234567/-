def max_guests(n, m):
    # n - общее количество этажей в отеле
    # m - количество номеров на этаже (кроме первого)
    floors_with_rooms = n - 1 # Количество этажей с номерами (исключая первый этаж)
    guests_per_rooms = 3       # Количество гостей в каждом номере
    total_guests = floors_with_rooms * m * guests_per_rooms # Общее количество гостей
    return total_guests       # Возвращаем общее количество гостей

print(max_guests(5, 10))
print(max_guests(10, 10))
print(max_guests(2, 5))
print(max_guests(1, 5))
print(max_guests(2, 1))
print(max_guests(1, 1))
