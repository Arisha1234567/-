def get_value(elem):
    if isinstance(elem, int):
        return elem
    elif isinstance(elem, list) and len(elem) == 1:
        return elem[0]
    else:
        raise ValueError("Недопустимый элемент: {}".format(elem))
def compare(e1, e2):
    val1 = get_value(e1)  #Возвращает True, если e1 < e2 по заданным правилам.
    val2 = get_value(e2)
    if val1 < val2:
        return True
    elif val1 > val2:
        return False
    else:
        # если один из элементов список, а другой число, то число считается меньшим.
        if isinstance(e1, int) and isinstance(e2, list):
            return True  # число < список
        elif isinstance(e1, list) and isinstance(e2, int):
            return False  # список > число
        else:
            # Оба числа или оба списка с одинаковым числом
            return False  # равны, ни одно не меньше другого
def sort_like_nums(nums):
    #Сортирует список nums по правилам выбором.
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if compare(nums[j], nums[min_idx]):
                min_idx = j
        # Обмен элементов
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
nums = [[4], 3, 2, [5], [1]]
sort_like_nums(nums)
print(nums)
nums = [2, 1, [2], 3, [3]]
sort_like_nums(nums)
print(nums)
nums = [[1]]
sort_like_nums(nums)
print(nums)
nums = [[1], 1]
sort_like_nums(nums)
print(nums)
nums = [[4], [3], [2], [5], [1]]
sort_like_nums(nums)
print(nums)
nums = [-1, [-1], [-2], -2, [-1]]
sort_like_nums(nums)
print(nums)
