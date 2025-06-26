def move_zeros(nums):
    # создаем новый список, включающий все ненулевые элементы
    non_zero_elements = [num for num in nums if num != 0]
    # подсчитываем кол-во нулей
    zero_count = nums.count(0)
    # расширяем список нулями в конце
    non_zero_elements.extend([0] * zero_count)
    # обновляем исходный список
    nums[:] = non_zero_elements
nums = [0, 1, 2]
move_zeros(nums)
print(nums)
nums = [0, 2, 1]
move_zeros(nums)
print(nums)
nums = [1, 2, 3]
move_zeros(nums)
print(nums)
nums = [1]
move_zeros(nums)
print(nums)
nums = [1, 1, 1, 1]
move_zeros(nums)
print(nums)
nums = [0, 0, 0]
move_zeros(nums)
print(nums)