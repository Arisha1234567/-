def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
print(binary_search([50, 40, 30, 20, 10], 30))
print(binary_search([50, 40, 30, 20, 10], 0))
print(binary_search([5, 4, 3, 2, 1], 5))
print(binary_search([5], 5))
print(binary_search([1, 0, -1], -1))
print(binary_search([5, 4, 3, 2, 1], 1))

