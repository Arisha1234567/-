def number_of_swaps(nums):
    swaps = 0
    n = len(nums)
    # используем классическую пузырьковую сортировку
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # обмен элементов
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaps += 1
    return swaps
print(number_of_swaps([1, 2, 4, 3, 5]))
print(number_of_swaps([2, 1, 4, 3, 5]))
print(number_of_swaps([1, 2, 3, 4, 5]))
print(number_of_swaps([5, 4, 3, 2, 1]))
print(number_of_swaps([1]))
print(number_of_swaps([2, 1]))
