def sum_of_seven_smallest(nums):
    # проверка, что в списке есть хотя бы 7 элементов
    if len(nums) < 7:
        raise ValueError("Список должен содержать хотя бы 7 элементов")

   
    import heapq
    seven_smallest = heapq.nsmallest(7, nums)
    return sum(seven_smallest)
print(sum_of_seven_smallest([2, 7, 3, 6, 10, 4, 1, 9, 5, 8]))
print(sum_of_seven_smallest([2, 2, 4, 1, 3, 3, 5, 4, 4]))
print(sum_of_seven_smallest([1, 1, 1, 1, 1, 1, 1, 1]))
print(sum_of_seven_smallest([-1, 1, -1, 1, -1, 1, -1, 1]))
print(sum_of_seven_smallest([-50, 15, 15, 20, 10, 15, 3, 2, 5]))
print(sum_of_seven_smallest([-7, -2, -2, -8, -1, -4, -10]))
