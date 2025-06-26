
def count_numbers(n, k):
    count = 0
    for i in range(1, n + 1):
        digit_sum = sum(int(d) for d in str(i))
        if i - digit_sum >= k:
            count += 1
    return count


print(count_numbers(13, 2))
print(count_numbers(10, 5))
print(count_numbers(1, 0))
print(count_numbers(10, 0))
print(count_numbers(10, 1))
print(count_numbers(10, 15))