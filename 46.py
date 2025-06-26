def third_max_value(nums):
    unique_nums = set(nums)

    if len(unique_nums) < 3 :
        return max(unique_nums)

    third_max = sorted(unique_nums, reverse=True)[2]
    return third_max
print(third_max_value([4, 8, 6, 10]))
print(third_max_value([4, 4, 4, 4]))
print(third_max_value([1, 2, 3]))
print(third_max_value([3, 2, 1]))
print(third_max_value([-1, -2, -3]))
print(third_max_value([4, 4, 2, 2, 1, 3, 5, 6]))
