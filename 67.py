def binary_insertion_sort(nums):
    import bisect

    for i in range(1, len(nums)):
        key = nums[i]
        # Находим позицию вставки с помощью бинарного поиска
        # Встроенная функция bisect_left возвращает позицию вставки для key
        insert_pos = bisect.bisect_left(nums, key, 0, i)

        nums.pop(i) # Вставляем элемент в найденную позицию
        nums.insert(insert_pos, key)



nums = [3, 4, 1, 2, 5]
binary_insertion_sort(nums)
print(nums)
nums = [3, 2, 2, 1, 3, 3]
binary_insertion_sort(nums)
print(nums)
nums = [1]
binary_insertion_sort(nums)
print(nums)
nums = [5, 4, 3, 2, 1]
binary_insertion_sort(nums)
print(nums)
nums = [-2, -10, -7, -6]
binary_insertion_sort(nums)
print(nums)
nums = [-3, -3, -3, -3]
binary_insertion_sort(nums)
print(nums)