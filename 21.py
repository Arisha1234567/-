def longest_substring_without_vowels(s: str) -> int:
    # Список гласных
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_length = 0  # Максимальная длина подстроки
    current_length = 0  # Текущая длина подстроки
    # Итерируем по символам строки
    for char in s:
        if char not in vowels:  # Если символ не гласная
            current_length += 1  # Увеличиваем текущую длину
        else:
            max_length = max(max_length, current_length)  # Обновляем максимальную длину
            current_length = 0  # Сбрасываем текущую длину

    max_length = max(max_length, current_length)  # Проверяем в конце
    return max_length  # Возвращаем максимальную длину

print(longest_substring_without_vowels('abcdefg'))
print(longest_substring_without_vowels('bcdgf'))
print(longest_substring_without_vowels('aeiou'))
print(longest_substring_without_vowels('abecidofug'))
print(longest_substring_without_vowels('x'))
print(longest_substring_without_vowels('abbbabbaba'))
