def find_index(nums, target):
    if not nums:
        return -1
    # Обработка случая, когда первый элемент равен цели
    if nums[0] == target:
        return 0
    index = 1
    n = len(nums)
    # Расширяем диапазон поиска
    while index < n and nums[index] < target:
        index *= 2
    # Устанавливаем левый и правый границы для двоичного поиска
    left = index // 2
    right = min(index, n - 1)
    # Двоичный поиск
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # если не нашли
    return -1


nums1 = [4 + 3 * i for i in range(100000)]
nums2 = [i * i for i in range(100000)]
print(find_index(nums1, 13))
print(find_index(nums1, 11))
print(find_index(nums1, 4))
print(find_index(nums2, 0))
print(find_index(nums2, 75345))
print(find_index(nums2, 9999800001))