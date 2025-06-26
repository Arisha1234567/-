def bounded_binary_search(nums, target, left=None, right=None) :
    n = len(nums)
    if left is None :
        left = 0
    if right is None :
        right = n - 1
    if left > right or left < 0 or right >= n :
        return -1

    while left <= right :
        mid = (left + right) // 2
        if nums[mid] == target :
            return mid
        elif nums[mid] < target :
            left = mid + 1
        else :
            right = mid - 1
    return -1
print(bounded_binary_search([10, 20, 30, 40, 50], 40))
print(bounded_binary_search([10, 20, 30, 40, 50], 60, left=0, right=4))
print(bounded_binary_search([1, 3, 5, 7, 9], 5, 1, 3))
print(bounded_binary_search([1, 3, 5, 7, 9], 5, 0, 1))
print(bounded_binary_search([1], 1,left=0))
print(bounded_binary_search([-1, 0, 1], -1, right=1))
