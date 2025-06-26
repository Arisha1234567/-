def min_digit_sum(a: int, b: int) -> int:
    min_sum = float('inf')
    count = 0

    for i in range(a, b + 1):
        current_sum = 0
        temp = i
        while temp > 0:
            current_sum += temp % 10
            temp //= 10

        if current_sum < min_sum:
            min_sum = current_sum
            count = 1
        elif current_sum == min_sum:
            count += 1

    return count
print(min_digit_sum(1, 50))
print(min_digit_sum(1, 100))
print(min_digit_sum(50, 200))
print(min_digit_sum(1, 1))
print(min_digit_sum(1, 1000))
print(min_digit_sum(456, 678))
