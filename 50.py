def binary_search(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    is_ascending = nums[0] < nums[-1]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if is_ascending:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1

    return -1
print(binary_search([10, 20, 30, 40, 50], 20))
print(binary_search([50, 40, 30, 20, 10], 20))
print(binary_search([10, 20, 30, 40, 50], 25))
print(binary_search([1], 1))
print(binary_search([-1, 0, 1], -1))
print(binary_search([1, 0, -1], -1))
