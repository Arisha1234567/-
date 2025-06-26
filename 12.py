def training_time(n, m, s, b):
    # n - количество раундов тренировки; m - минуты в раунде; s - секунды в раунде; b - секунды отдыха
    total_seconds = n * (m * 60 + s) + (n - 1) * b # общее время в секундах
    total_minutes = total_seconds // 60 # общее время в минутах
    remaining_seconds = total_seconds % 60 # остаток секунд
    return(total_minutes, remaining_seconds) # возвращает минуты и секунды

print(training_time(3, 2, 10, 90))
print(training_time(1, 1, 0, 0))
print(training_time(1, 0, 1, 0))
print(training_time(1, 1, 1, 1))
print(training_time(2, 1, 1, 0))
print(training_time(1, 1, 0, 1))




