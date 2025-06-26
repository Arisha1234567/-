def alter_sort(nums):
    # сортируем список по возрастанию с помощью сортировки выбором
    n = len(nums)
    for i in range(n):
        # ищем индекс минимального элемента в оставшейся части списка
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # меняем местами
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    # cоздаём новый список
    result = []
    left = 0
    right = n - 1
    while left <= right:
        if right >= left:
            result.append(nums[right])  # максимум
            right -= 1
        if left <= right:
            result.append(nums[left])  # минимум
            left += 1

    # Модифицируем исходный список
    for i in range(n):
        nums[i] = result[i]
nums = [1, 2, 3, 4, 5]
alter_sort(nums)
print(nums)
nums = [5, 4, 3, 2, 1]
alter_sort(nums)
print(nums)
nums = [1, 1, 1]
alter_sort(nums)
print(nums)
nums = [2, 3, 1, 5, 5, 3, 1]
alter_sort(nums)
print(nums)
nums = [-1, -5, -3, -2, -7, -4]
alter_sort(nums)
print(nums)
nums = [2]
alter_sort(nums)
print(nums)