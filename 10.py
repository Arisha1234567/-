def swap_digits(n):
    first_digit = n // 100 # Находим первую цифру
    midd_ledigit = (n // 10) % 10 # Находим среднюю цифру
    lastdigit = n % 10 # Находим последнюю цифру
    return lastdigit * 100 + midd_ledigit * 10 + first_digit # Возвращаем число с переставленными цифрами

print(swap_digits(123))
print(swap_digits(321))
print(swap_digits(555))
print(swap_digits(545))
print(swap_digits(550))
print(swap_digits(500))





