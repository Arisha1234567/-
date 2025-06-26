def avg_values(nums: list) -> list:
    if not nums:
        return []

    result = []
    total = 0
    for i, num in enumerate(nums):
        total += num
        average = total / (i + 1)
        result.append(average)
    return result

print(avg_values([10, 20, 30, 40, 50]))
print(avg_values([1, 1, 1, 1, 1]))
print(avg_values([-2, -3, 5, 5]))
print(avg_values([]))
print(avg_values([0, 0, 0, 0]))
print(avg_values([3]))

