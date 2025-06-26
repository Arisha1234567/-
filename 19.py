def sum_of_squares(n: int) -> int:
    # Вычисляем сумму квадратов первых n натуральных чисел по формуле
    return n * (n + 1) * (2 * n + 1) // 6  # Возвращаем результат


print(sum_of_squares(1))
print(sum_of_squares(2))
print(sum_of_squares(3))
print(sum_of_squares(5))
