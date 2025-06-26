def linear_search(nums, target, reverse=False):
    if reverse:
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                index = i
        return index
    else:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
print(linear_search([1, 5, 7], 5))
print(linear_search([2, 1, 7, 2], 2))
print(linear_search([12, 4, 1], 9))
print(linear_search([], 0))
print(linear_search([-2, 1, 7, -2], -2, reverse=True))
print(linear_search([1], 1))

