def divisible(n: int) -> int:
    count = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit != 0 and n % digit == 0:
            count += 1
        temp //= 10
    return count

print(divisible(22))
print(divisible(500))
print(divisible(1))
print(divisible(11))
print(divisible(2340))
print(divisible(23))


