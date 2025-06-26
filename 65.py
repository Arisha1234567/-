def cocktail_sort(nums):
    n = len(nums)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(left, right):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        right -= 1

        if not swapped:
            break

        swapped = False

        for i in range(right, left, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                swapped = True
        left += 1


data = [8, 9, 6, 5, 7, 4, 1, 2, 3]
cocktail_sort(data)
print(data)

data = [5, 4, 3, -2, 1]
cocktail_sort(data)
print(data)

data = [3]
cocktail_sort(data)
print(data)

data = [1, 2, 3, 4, 5]
cocktail_sort(data)
print(data)

data = [2, 1]
cocktail_sort(data)
print(data)

data = [1, 1, 1, 1, 1]
cocktail_sort(data)
print(data)