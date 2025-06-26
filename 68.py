def section_sort(nums):
    start = 0
    n = len(nums)
    for i in range(n + 1):
        # Когда достигается конец списка или встречается ноль
        if i == n or nums[i] == 0:
            # Отсортируем подпоследовательность
            nums[start:i] = sorted(nums[start:i])
            start = i + 1  # Начинаем новую подпоследовательность после нуля
nums = [2, 1, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)
nums = [1, 1, 1, 0, 5, 3, 4, 0, 2, 5, 3, 0, 3, 2, 1, 0]
section_sort(nums)
print(nums)
nums = [1, 1, 1, 0, 2, 2, 2, 0]
section_sort(nums)
print(nums)
nums = [3, 2, 1, 0]
section_sort(nums)
print(nums)
nums = [1, 0]
section_sort(nums)
print(nums)
nums = [5, 4, 3, 0, 2, 1, 0]
section_sort(nums)
print(nums)