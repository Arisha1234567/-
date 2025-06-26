def time_zone(h, a, b):
    # h - текущее время; a - часовой пояс Артура; b - часовой пояс местонахождения
    arthur_time = h + (b - a) # Время у Артура с учетом разницы часовых поясов
    return arthur_time % 24 # Время у Артура по модулю 24 (чтобы оставаться в пределах суток)

print(time_zone(12, 3, 7))
print(time_zone(12, -4, 4))
print(time_zone(12, 0, 0))
print(time_zone(0, 0, 0))
print(time_zone(6, -11, 12))
print(time_zone(23, 12, -11))
